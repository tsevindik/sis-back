###Automate Deployment

**In Server**
- Initialize bare repo
```
cd /home/ubuntu/projects/sis-back/
git init --bare .git
```
- Copy post receive hook
```
cp ./setup/hooks/post-receive ./.git/hooks/post-receive
```
- Make it executable
```
chmod +x ./.git/hooks/post-receive
```

**In Local**
- Add remote
```
git remote add ssh://ubuntu@ip-172-31-23-18/home/ubuntu/projects/sis-back/.git
```
- Add ssh private key
```
ssh-add key.pem
```
- Push (You can only push master and do not forget to setup server before anything else)
```
git push origin master
```
