#!/usr/bin/env python3
"""
DAK Post-Processing Integration Script

This script can be called after the FHIR IG Publisher runs to add DAK-specific
post-processing including JSON schemas, JSON-LD vocabularies, and API documentation.

It downloads and runs the necessary scripts from the smart-base repository.

Usage:
    python dak_processor.py [--output-dir output] [--source-dir .]

Author: SMART Guidelines Team
"""

import os
import sys
import subprocess
import logging
import argparse
import json
from pathlib import Path
import urllib.request
import tempfile
from datetime import datetime


def setup_logging():
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


class DAKProcessor:
    """Handles DAK post-processing after FHIR IG Publisher runs."""
    
    def __init__(self, logger, output_dir="output", source_dir="."):
        self.logger = logger
        self.output_dir = os.path.abspath(output_dir)
        self.source_dir = os.path.abspath(source_dir)
        self.temp_dir = tempfile.mkdtemp(prefix="dak_processor_")
        self.scripts_base_url = "https://raw.githubusercontent.com/WorldHealthOrganization/smart-base/main/input/scripts"
        self.includes_base_url = "https://raw.githubusercontent.com/WorldHealthOrganization/smart-base/main/input/includes"
        
        # Scripts we need for DAK processing
        self.required_scripts = [
            "generate_valueset_schemas.py",
            "generate_logical_model_schemas.py", 
            "generate_jsonld_vocabularies.py",
            "generate_dak_api_hub.py"
        ]
        
        # Include files we might need
        self.include_files = [
            "dmn2html.xslt",
            "dmn.css"
        ]
    
    def download_file(self, url, local_path):
        """Download a file from URL to local path."""
        try:
            self.logger.info(f"Downloading {url}")
            urllib.request.urlretrieve(url, local_path)
            return True
        except Exception as e:
            self.logger.warning(f"Failed to download {url}: {e}")
            return False
    
    def download_dak_scripts(self):
        """Download required DAK processing scripts."""
        scripts_dir = os.path.join(self.temp_dir, "scripts")
        os.makedirs(scripts_dir, exist_ok=True)
        
        downloaded_scripts = []
        
        # Download main processing scripts
        for script in self.required_scripts:
            url = f"{self.scripts_base_url}/{script}"
            local_path = os.path.join(scripts_dir, script)
            
            if self.download_file(url, local_path):
                os.chmod(local_path, 0o755)  # Make executable
                downloaded_scripts.append(local_path)
                self.logger.info(f"✅ Downloaded {script}")
            else:
                self.logger.warning(f"⚠️ Failed to download {script}")
        
        # Download include files if needed
        includes_dir = os.path.join(self.temp_dir, "includes")
        os.makedirs(includes_dir, exist_ok=True)
        
        for include_file in self.include_files:
            url = f"{self.includes_base_url}/{include_file}"
            local_path = os.path.join(includes_dir, include_file)
            
            if self.download_file(url, local_path):
                self.logger.info(f"✅ Downloaded {include_file}")
        
        return downloaded_scripts
    
    def check_dak_enabled(self):
        """Check if DAK processing should be enabled for this repository."""
        # Check for dak.json file
        dak_json_path = os.path.join(self.source_dir, "dak.json")
        if os.path.exists(dak_json_path):
            try:
                with open(dak_json_path, 'r') as f:
                    dak_config = json.load(f)
                self.logger.info(f"✅ Found dak.json - DAK processing enabled")
                return True
            except Exception as e:
                self.logger.warning(f"Found dak.json but couldn't parse it: {e}")
        
        # Check if smart.who.int.base is a dependency
        sushi_config_path = os.path.join(self.source_dir, "sushi-config.yaml")
        if os.path.exists(sushi_config_path):
            try:
                import yaml
                with open(sushi_config_path, 'r') as f:
                    sushi_config = yaml.safe_load(f)
                
                dependencies = sushi_config.get('dependencies', {})
                if 'smart.who.int.base' in dependencies:
                    self.logger.info("✅ Found smart.who.int.base dependency - DAK processing enabled")
                    return True
            except Exception as e:
                self.logger.warning(f"Could not check sushi-config.yaml: {e}")
        
        self.logger.info("ℹ️ DAK processing not enabled (no dak.json or smart.who.int.base dependency)")
        return False
    
    def run_script(self, script_path, args=None):
        """Run a Python script with the given arguments."""
        if not os.path.exists(script_path):
            self.logger.error(f"Script not found: {script_path}")
            return False
        
        cmd = [sys.executable, script_path]
        if args:
            cmd.extend(args)
        
        try:
            self.logger.info(f"Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, cwd=self.source_dir, capture_output=True, text=True, timeout=300)
            
            if result.stdout:
                self.logger.info(f"Script output: {result.stdout}")
            if result.stderr:
                self.logger.warning(f"Script stderr: {result.stderr}")
            
            if result.returncode == 0:
                self.logger.info(f"✅ Script completed successfully: {os.path.basename(script_path)}")
                return True
            else:
                self.logger.warning(f"⚠️ Script completed with errors: {os.path.basename(script_path)} (exit code: {result.returncode})")
                return False
                
        except subprocess.TimeoutExpired:
            self.logger.error(f"❌ Script timed out: {os.path.basename(script_path)}")
            return False
        except Exception as e:
            self.logger.error(f"❌ Error running script {os.path.basename(script_path)}: {e}")
            return False
    
    def process(self):
        """Main processing method."""
        self.logger.info("🔬 Starting DAK post-processing...")
        
        # Check if DAK processing should be enabled
        if not self.check_dak_enabled():
            self.logger.info("DAK processing not enabled, skipping...")
            return True
        
        # Check if output directory exists
        if not os.path.exists(self.output_dir):
            self.logger.error(f"Output directory not found: {self.output_dir}")
            self.logger.error("Please run the FHIR IG Publisher first to generate the output directory")
            return False
        
        self.logger.info(f"Processing output directory: {self.output_dir}")
        
        # Download required scripts
        scripts = self.download_dak_scripts()
        if not scripts:
            self.logger.error("No DAK scripts could be downloaded")
            return False
        
        success_count = 0
        total_scripts = 0
        
        # 1. Generate ValueSet schemas
        valueset_script = os.path.join(self.temp_dir, "scripts", "generate_valueset_schemas.py")
        if os.path.exists(valueset_script):
            total_scripts += 1
            self.logger.info("📊 Generating ValueSet schemas...")
            expansions_file = os.path.join(self.output_dir, "expansions.json")
            if os.path.exists(expansions_file):
                if self.run_script(valueset_script, [expansions_file, self.output_dir]):
                    success_count += 1
            else:
                self.logger.warning("expansions.json not found, skipping ValueSet schema generation")
        
        # 2. Generate Logical Model schemas
        lm_script = os.path.join(self.temp_dir, "scripts", "generate_logical_model_schemas.py")
        if os.path.exists(lm_script):
            total_scripts += 1
            self.logger.info("📋 Generating Logical Model schemas...")
            if self.run_script(lm_script, [self.output_dir, self.output_dir]):
                success_count += 1
        
        # 3. Generate JSON-LD vocabularies
        jsonld_script = os.path.join(self.temp_dir, "scripts", "generate_jsonld_vocabularies.py")
        if os.path.exists(jsonld_script):
            total_scripts += 1
            self.logger.info("🗂️ Generating JSON-LD vocabularies...")
            expansions_file = os.path.join(self.output_dir, "expansions.json")
            if os.path.exists(expansions_file):
                if self.run_script(jsonld_script, [expansions_file, self.output_dir]):
                    success_count += 1
            else:
                self.logger.warning("expansions.json not found, skipping JSON-LD vocabulary generation")
        
        # 4. Generate DAK API Hub
        api_script = os.path.join(self.temp_dir, "scripts", "generate_dak_api_hub.py")
        if os.path.exists(api_script):
            total_scripts += 1
            self.logger.info("🌐 Generating DAK API Hub...")
            openapi_dir = os.path.join(self.source_dir, "input", "images", "openapi")
            if self.run_script(api_script, [self.output_dir, openapi_dir]):
                success_count += 1
        
        # Summary
        self.logger.info(f"DAK post-processing completed: {success_count}/{total_scripts} scripts successful")
        
        if success_count == total_scripts:
            self.logger.info("✅ All DAK post-processing completed successfully!")
            return True
        elif success_count > 0:
            self.logger.warning(f"⚠️ Partial success: {success_count}/{total_scripts} scripts completed")
            return True
        else:
            self.logger.error("❌ DAK post-processing failed")
            return False
    
    def cleanup(self):
        """Clean up temporary files."""
        try:
            import shutil
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            self.logger.info("🧹 Cleaned up temporary files")
        except Exception as e:
            self.logger.warning(f"Warning: Could not clean up temporary files: {e}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="DAK Post-Processing for FHIR Implementation Guides"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Directory containing FHIR IG Publisher output (default: output)"
    )
    parser.add_argument(
        "--source-dir", 
        type=str,
        default=".",
        help="Source directory of the IG repository (default: current directory)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force DAK processing even if dak.json is not found"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    logger = setup_logging()
    
    # Initialize processor
    processor = DAKProcessor(logger, args.output_dir, args.source_dir)
    
    try:
        # Override DAK enabled check if force is specified
        if args.force:
            logger.info("🔧 Force mode enabled - DAK processing will run regardless of configuration")
            original_check = processor.check_dak_enabled
            processor.check_dak_enabled = lambda: True
        
        # Run processing
        success = processor.process()
        
        # Exit with appropriate code
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        logger.info("❌ DAK processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error during DAK processing: {e}")
        sys.exit(1)
    finally:
        processor.cleanup()


if __name__ == "__main__":
    main()
