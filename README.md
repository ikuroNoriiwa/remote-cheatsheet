# remote cheatsheet 

This project was created to use locally cheatsheet located on remote server using wikiJS to store them. 

## Installation 
```
git clone git@github.com:ikuroNoriiwa/remote-cheatsheet.git
cd remote-cheatsheet 
python3 -m pip install -r requirements.txt 
```

## Usage 
### First time 
Before using the app, you have to configure it. 
It require to have an API token on wikiJS (It actually only support wiki.hades-cybersecruity.com server, but multi tenant will be added in the future)
Then you can run the init configuration command : 

```
python3 -m cheatsheet config init-config <token>
```

This command will create the configuration directory located at `$HOME/.wiki-cheatsheet` containing a `cheatsheet` directory, a sqlite database and a file `token.md` containing your API token (will be replaced in the future)

### Download Cheatsheet 
Actually, the tool allow you to download every cheatsheets on remote server, or single cheatsheet using its ID. 

#### Download all 
To download all cheatsheets, use the following command : 
```
python3 -m cheatsheet remote download-all
```

#### Download Specific cheatsheet 
You can list all remote cheatsheets using the command : 
```
python3 -m cheatsheet remote list-all 
```

Now you see the ID of each cheatsheet, you can download specific one: 
``` 
python3 -m cheatsheet remote download <CHEATSHEET_ID>
``` 

### Using local cheatsheet 
Once you download some cheatsheets, you can use local module. 
The local module is a copy of the remote cheatsheets that you can use offline. 
you can list all local cheatsheet : 
```
python3 -m cheatsheet local list 
```

You also can read specific cheatsheet using its id 
```
python3 -m cheatsheet local read <CHEATSHEET_ID>
```

## Next steps
The project is actually under developpement status and will improve during the next months. the feature that are in projects : 

- [] Synchronize remote and local 
- [] Synchronize local and remote 
- [] add the possibility to edit/create sheets and upload them 
- [~] use more functionality with tags 
- [] Multi site compatibility (WIkiJS only)
- [] Support other types of sites (ex: Github ? )
- [] parsing of cheatsheets 
- [] autocompletion using cheatsheets content 
- [] plugin option 