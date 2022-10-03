import view
import model

def selection_menu():
    res = view.user_menu()
    if res == 1:
        view.view_user(model.show_users())
    elif res == 2:
        model.create_user(view.user_data_entry())
    elif res == 3:
        view.view_user(model.show_users())
        lst_user = model.show_users()
        num = view.up_del_user()
        model.new_create_user(model.delete_user(num, lst_user))
        view.view_user(model.show_users())
    elif res == 4:
        view.view_user(model.show_users())
        lst_user = model.show_users()
        res = model.update_user(view.up_del_user(), lst_user)
        model.new_create_user(res)
        view.view_user(model.show_users())
    elif res == 5:
        lst_user = model.show_users()
        model.txt_creator(lst_user)
    elif res == 6:
        lst_user = model.show_users()
        model.json_creator(lst_user)
    elif res == 7:
        lst_user = model.show_users()
        model.xml_creator(lst_user)
