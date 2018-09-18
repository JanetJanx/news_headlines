from newsheadlines import cli
from click.testing import CliRunner


class TestNews():
    def test_cli_function():
        runner = CliRunner()
        result = runner.invoke(cli, ['1'])
        url = url="https://newsapi.org/v2/top-headlines?sources=fox-news&apiKey=9b40cf73093e47e586cd61132f1d56fe&pageSize=10"
        expected_output = [requests.get(url).json()['articles']]
        assert result.exit_code, 0
        assert result.output, expected_output
        
    
TestNews.test_cli_function()
