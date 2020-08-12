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
 $ sed -i 's/localhost/<server IP>/g' main.475e8a0b11d99136261f.js
 $ http-server
 Available on:
  http://127.0.0.1:8080
  http://172.31.25.851:8080

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
 $ vi routes.json
	{
		"/api/*": "/$1",
		"/:resource/:id/show": "/:resource/:id",
		"/posts/:category": "/posts?category=:category",
		"/articles\\?id=:id": "/posts/:id"
	}

 $ sudo chmod -R 777 App #Give full permission to App Folder
 
 #Note** :- Restart the server
 
 ~/App/server$ json-server --watch db.json -H <http-server generated IP '172.31.25.851' > --routes routes.json
