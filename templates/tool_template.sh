#!/bin/bash

# {{TOOL_NAME}} - {{DESCRIPTION}}
# Usage: ./{{TOOL_NAME}} {{USAGE_EXAMPLE}}
# REQUIRES: {{REQUIRED_COMMANDS}}

{{PARAMETER_VALIDATION}}

# Use working directory for temporary files to avoid permission issues
TMP_DIR="./tmp_{{TOOL_NAME}}_$$"
mkdir -p "$TMP_DIR"
trap "rm -rf $TMP_DIR" EXIT

# Check and auto-install dependencies
{{DEPENDENCY_CHECKS}}

# {{MAIN_FUNCTIONALITY_COMMENT}}
echo "{{ACTION_MESSAGE}}"

{{IMPLEMENTATION_PLACEHOLDER}}

echo "{{SUCCESS_MESSAGE}}"