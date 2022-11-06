Clone repo
	Get HTTPS clone link
	git clone <clone link>

Add files to index
	git add <file1> <file2> ...

Add all files to index (while in base directory)
	git add .

Remove files from index
	git restore --staged <file1> <file2> ...

Remove all files from index (while in base directory)
	git restore --staged .

Commit changes
	git commit -m "<message>"

Commit all (tracked) modified files
	git commit -a

Push changes
	git push

Pull changes
	git pull origin

Create branch
	git branch <branch>

List branches
	git branch

Switch branches
	git switch <branch>

Delete branch
	git branch -D <branch>

Set credentials
	git config user.name "<name>"
	git config user.email "<email>"
	git config --global user.name "<name>"
	git config --global user.email "<email>"

Check credentials
	git config user.name
	git config user.email
	git config --global user.name
	git config --global user.email

Unset password
	git config --global --unset user.password

Get repo base path
	git rev-parse --show-toplevel


==================================================================
.gitignore help
==================================================================

`folder_name/` will ignore all instances of `folder_name`
`/folder_name/` will ignore specifically the folder at the root
