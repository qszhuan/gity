from gitx import Gitx
import mock

@mock.patch('gitx.Gitx._remote_url', return_value='git@github.com:qszhuan/git-x.git')
@mock.patch('gitx.Gitx._current_branch', return_value='abc')
@mock.patch('gitx.open_url', return_value=0)
def test_pr_with_git_remote_origin(mock_open_url, mock_current_branch, mock_remote_url):
    branch = 'master'
    Gitx().pr(branch)
    mock_remote_url.assert_called()
    mock_current_branch.assert_called()
    mock_open_url.assert_called_once_with('https://github.com/qszhuan/git-x/compare/master...abc?expand=1')



@mock.patch('gitx.Gitx._remote_url', return_value='https://github.com/qszhuan/git-x.git')
@mock.patch('gitx.Gitx._current_branch', return_value='abc')
@mock.patch('gitx.open_url', return_value=0)
def test_pr_with_https_remote_origin(mock_open_url, mock_current_branch, mock_remote_url):
    branch = 'master'
    Gitx().pr(branch)
    mock_remote_url.assert_called()
    mock_current_branch.assert_called()
    mock_open_url.assert_called_once_with('https://github.com/qszhuan/git-x/compare/master...abc?expand=1')