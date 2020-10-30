def pytest_addoption(parser):
    parser.addoption("--nice", action = "store", help = "A nice way to print output")


def pytest_report_header(config):
    if config.getoption("nice"):
        return "Thanks for using my plugin"


def pytest_report_teststatus(report, config):
    if report.when == "call":
        if report.failed and config.getoption("nice"):
            return (report.outcome, "D", "Dinesh to change these" )



