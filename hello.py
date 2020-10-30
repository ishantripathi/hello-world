#!/bin/python
print("This is python demo file")

def get_data(doc_id):
    global inlink_catlaog
    global inlink_path
    with open(inlink_path, 'r') as inl_file:
        offset = inlink_catlaog[doc_id][0]
        inl_file.seek(offset)
        line = inl_file.readline()
        return line


def get_inlink_list(doc_id):
    line = get_data(doc_id)
    inlink_list = line.split()[1:]
    inlink_list_set = set(inlink_list)
    # inlink_list_set.remove(doc_id)
    return inlink_list_set


for (int i=0; i<10; i++){
get_data[]
    get_inlink_list[]
    
}
