import pytest

def pytest_addoption(parser):
    group = parser.getgroup("nice")
    group.addoption("--nice", action="store_true", help = "Prints the outputs in a nicer way")


def pytest_report_header(config):
    print("The pytest option is", config.getoption("nice"))
    if config.getoption("nice"):
        print(" Inside if condition ")
        return "\n---------------Thanks for using this plugin-----------------\n"


def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.failed and config.getoption("nice"):
            return (report.outcome, "O", "Opportunity for improvement")
