#!/bin/bash

# ============================================
# Test Runner for Decimal to Any Base Converter
# ============================================

# Colors for pretty output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

show_help() {
    echo ""
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE}  Decimal to Any Base Converter - Tests    ${NC}"
    echo -e "${BLUE}============================================${NC}"
    echo ""
    echo "Usage: ./run_tests.sh [option]"
    echo ""
    echo "Options:"
    echo "  (none)      Run all tests with verbose output"
    echo "  coverage    Run tests with coverage report"
    echo "  quiet       Run tests with minimal output"
    echo "  failed      Run only previously failed tests"
    echo "  specific    Run a specific test class (will prompt)"
    echo "  help        Show this message"
    echo ""
    echo "Examples:"
    echo "  ./run_tests.sh"
    echo "  ./run_tests.sh coverage"
    echo "  ./run_tests.sh quiet"
    echo ""
}

check_pytest() {
    if ! python3 -c "import pytest" 2>/dev/null; then
        echo -e "${YELLOW}pytest is not installed.${NC}"
        echo ""
        echo "To install pytest, run one of the following:"
        echo "  pip3 install pytest"
        echo "  pip install pytest"
        echo "  sudo apt install python3-pytest"
        echo ""
        exit 1
    fi
}

run_verbose() {
    echo ""
    echo -e "${GREEN}Running all tests (verbose mode)...${NC}"
    echo ""
    python3 -m pytest test_convert.py -v
}

run_coverage() {
    echo ""
    
    # Check if pytest-cov is installed
    if ! python3 -c "import pytest_cov" 2>/dev/null; then
        echo -e "${YELLOW}pytest-cov is not installed.${NC}"
        echo ""
        echo "To install pytest-cov, run one of the following:"
        echo "  pip3 install pytest-cov"
        echo "  pip install pytest-cov"
        echo ""
        exit 1
    fi
    
    echo -e "${GREEN}Running tests with coverage report...${NC}"
    echo ""
    python3 -m pytest test_convert.py -v --cov=convert --cov-report=term-missing
}

run_quiet() {
    echo ""
    echo -e "${GREEN}Running tests (quiet mode)...${NC}"
    echo ""
    python3 -m pytest test_convert.py -q
}

run_failed() {
    echo ""
    echo -e "${GREEN}Running only previously failed tests...${NC}"
    echo ""
    python3 -m pytest test_convert.py -v --lf
}

run_specific() {
    echo ""
    echo -e "${BLUE}Available test classes:${NC}"
    echo "  1) TestSpecialCases"
    echo "  2) TestIntegerConversion"
    echo "  3) TestBase2"
    echo "  4) TestBase10"
    echo "  5) TestBase60"
    echo "  6) TestNumbersGreaterThanOne"
    echo "  7) TestNegativeNumbers"
    echo "  8) TestRepeatingNumbers"
    echo "  9) TestAlgorithmDirectly"
    echo "  10) TestMainFunction"
    echo ""
    read -p "Enter the number of the test class to run: " choice
    
    case $choice in
        1) class="TestSpecialCases" ;;
        2) class="TestIntegerConversion" ;;
        3) class="TestBase2" ;;
        4) class="TestBase10" ;;
        5) class="TestBase60" ;;
        6) class="TestNumbersGreaterThanOne" ;;
        7) class="TestNegativeNumbers" ;;
        8) class="TestRepeatingNumbers" ;;
        9) class="TestAlgorithmDirectly" ;;
        10) class="TestMainFunction" ;;
        *)
            echo -e "${YELLOW}Invalid choice. Running all tests.${NC}"
            run_verbose
            return
            ;;
    esac
    
    echo ""
    echo -e "${GREEN}Running $class...${NC}"
    echo ""
    python3 -m pytest test_convert.py::$class -v
}

# Check for pytest before doing anything
check_pytest

# Main script logic
case "$1" in
    coverage)
        run_coverage
        ;;
    quiet)
        run_quiet
        ;;
    failed)
        run_failed
        ;;
    specific)
        run_specific
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        run_verbose
        ;;
    *)
        echo -e "${YELLOW}Unknown option: $1${NC}"
        show_help
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}Done!${NC}"
echo ""