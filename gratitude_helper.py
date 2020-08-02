
json_data = {
    "pandas": [
        ['username1', 'profile_pic1', 'profile1'],
        ['username2', 'profile_pic2', 'profile2'],
        ['username3', 'profile_pic3', 'profile3'],
        ['username4', 'profile_pic4', 'profile4'],
        ['username5', 'profile_pic5', 'profile5'] 
    ],
    "numpy": [
        ['username1', 'profile_pic1', 'profile1'],
        ['username2', 'profile_pic2', 'profile2'],
        ['username3', 'profile_pic3', 'profile3'],
        ['username4', 'profile_pic4', 'profile4'],
        ['username5', 'profile_pic5', 'profile5'] 
    ],
    "requests": [
        ['username1', 'profile_pic1', 'profile1'],
        ['username2', 'profile_pic2', 'profile2'],
        ['username3', 'profile_pic3', 'profile3'],
        ['username4', 'profile_pic4', 'profile4'],
        ['username5', 'profile_pic5', 'profile5'] 
    ],
}

data = {
    'name': "project_Name",
    'children': [
        
    ]
}
for module_name, module_data in json_data.items():
    username_s = []
    for i in module_data:
        username_s.append({"name": i[0]})

    data['children'].append({
        "name": module_name,
        "children": username_s
    })

    
print(data)
