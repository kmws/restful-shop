from models.group import Group


def get_group_by_name(group_name: str):
    group = Group.query.filter_by(name=group_name).first()
    return group
