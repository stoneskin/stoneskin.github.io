# Git.02 Use SmartGit as git client

## 1. Install SmartGit

- download SmartGit from <https://www.syntevo.com/smartgit/>, chose the version match your operating system
![downlaod smartgit](Git_02_DownloadSamrtGit.png)

- for windows, it will download a zip file, please open it and run the setup.exe file with Extract All.
![unzip smartgit](Git_02_unzipSamrtGit.png)

- Chose `No-commercial license` during you install the SmartGit
    - Install SmartGit [step by step](installSmartGit/installSmargGit.md) 

## 2. Create a repository in your github account

- In your github home page, click the  create new icon or click Start a project button
![](Git_02_NewRepository_2.png)      ![](Git_02_NewRepository_1.png)

- Input your name of project, and create your first repository
  ![](Git_02_CreateYourFirstProjectRepository.png)

- go to you repository page, ex https://github.com/{youracctname}/myproject, get the Clone url
![](Git_02_GetyourRepositoryCloneUrl.png)

## 3. SmartGit Clone your new project repository

- In SmartGit, Repository -> Clone
  ![](Git_02_SmartGitCloneYourProject.png)

- If you copy the url, the url will auto loaded to the Remote repository
  ![](Git_02_SmartGitCloneYourProjectStep1.png)

- click next
  ![](Git_02_SmartGitCloneYourProjectStep2.png)

- chose your project position 
  ![](Git_02_SmartGitCloneYourProjectStep3.png)

## 4. Add your code to the Working folder

- Add some code to your working folder, it will show on the `working Tree`
![](Git_02_WorkingTree.png)

- You could select the file you want to stage, and click stage button
![](Git_02_StageAndCommit.png)

- You also could skip the Stage step, can commit what you selected for commint
![](Git_02_CommitWithoutStagel.png)

- After commit, the committed files change will not on the Working Tree
![](Git_02_AfterCommit.png)

## 5. Push you change to the remote

- There are Pull, Sync, Push button on the top of the manual bar
![](Git_02_Pushbutton.png)

  - Pull is get change from remote to local
  - Sync is to make local and remote same, both have latest change
  - Push is just send you local change to remote server

- First time you push the code to remote github, you will be asking username and password
  
  ![github logoin](installSmartGit/smartgit_16_githublogin.png)

- If you need change username password, got to menu ->Edit ->Preference

  ![update password](installSmartGit/smartgit_17_UpdateAuthentication.png)

- After click Sync or Push, your local committed code will show on the github
  