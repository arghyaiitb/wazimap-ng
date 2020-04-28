from guardian.shortcuts import (
    get_group_perms, get_perms_for_model, get_groups_with_perms
)

def get_user_groups_with_permission_on_object(obj, user):
    user_groups = user.groups.all()
    groups_with_permission = get_groups_with_perms(obj)

    groups = [g for g in user_groups if g in groups_with_permission]
    return groups

def get_user_groups_without_permission_on_object(obj, user):
    user_groups = user.groups.all()
    user_groups_with_permission = get_user_groups_with_permission_on_object(obj, user)

    return [g for g in user_groups if g not in user_groups_with_permission]

def has_dataset_permissions(user, obj, permission):
    if not hasattr(obj, "dataset"):
        return None

    dataset = obj.dataset
    is_delete_permission = "delete" in permission.lower()

    if dataset.permission_type == "public" and not is_delete_permission:
        return True

    return user.has_perm(permission, dataset)

def has_permission(user, obj, permission):
    if user.is_superuser:
        return True

    dataset_permissions = has_dataset_permissions(user, obj, permission)
    if dataset_permissions is not None:
        return dataset_permissions

    return user.has_perm(permission, obj)

def has_owner_permission(user, obj, permission):
    if user.is_superuser:
        return True

    return user.has_perm(permission, obj)
