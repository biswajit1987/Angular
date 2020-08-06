# Angular

Mor more information on build :- https://angular.io/guide/build

For deployment : https://angular.io/guide/deployment

$ sudo apt-get update
 $ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
 $ sudo apt-get install nodejs
 $ sudo npm install -g json-server
 $ sudo npm i json-server
 $ sudo npm install --global http-server
 $ mkdir App
 $ cd App
 $ sudo git clone https://github.com/biswajit1987/Angular.git
 $ cd ~/App/Angular
 $ http-server
 ---------------------------
 Open new Terminal
 ---------------------------
 $ cd App
 $ mkdir server
 $  ls App
      Angular  server
 $ cd server/
 $ vi db.json
    {
       "users": [

         ]
    }

 :~/App/server$ json-server --watch db.json
