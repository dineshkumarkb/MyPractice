def pytest_addoption(parser):
    parser.addoption("--testnice", action="store", help="Change Request")

def pytest_report_header(config):
    if config.getoption("testnice"):
        return "\n\t\t-------------------Thanks for using my plugin-------------------------\n"

def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.failed and config.getoption("testnice"):
            return (report.outcome, "D", "Change Request to improve")