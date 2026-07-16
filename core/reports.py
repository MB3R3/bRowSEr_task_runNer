from core.utils import ensure_directory, timestamp
from config.settings import REPORT_DIR



def create_report(task, status, duration, error=None, output_file=None):

    ensure_directory(REPORT_DIR)

    filename = f"report_{timestamp()}.html"

    filepath = REPORT_DIR / filename

    html = f"""
    <html>
    <head>
        <title>Automation Report</title>
    </head>

    <body>

    <h1>Browser Task Runner</h1>

    <table border="1" cellpadding="10">

        <tr>
            <td>Task</td>
            <td>{task}</td>
        </tr>

        <tr>
            <td>Status</td>
            <td>{status}</td>
        </tr>

        <tr>
            <td>Duration</td>
            <td>{duration:.2f} seconds</td>
        </tr>

        <tr>
            <td>Output</td>
            <td>{output_file}</td>
        </tr>

        <tr>
            <td>Error</td>
            <td>{error}</td>
        </tr>

    </table>

    </body>

    </html>
    """

    filepath.write_text(html, encoding="utf-8")
    return filepath