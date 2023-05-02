from wiki_cheatsheet import cheatsheet

if __name__ == "__main__": 
    cs = cheatsheet()
    #print(cs.get_tag_list())
    """
    title, description, content, err =  cs.retrieve_page_by_id(1)
    if err is None: 
        with open(title.replace(" ", "_") + ".md", "w") as file: 
            file.write(content)
    else: 
        print(err)
    """
    #title, description, content, err =  cs.retrieve_page_by_id(13)
    #print(content)
    #cs.get_page_id_by_tags(["enum"])
    #cs.init_config()
    #cs.init_local_db()
    #cs.simulate_data()
    cs.search_term_in_name("f")

