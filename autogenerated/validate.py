VERSION = "2.16.2"


NoneType = type(None)

def validate_https___spl_robocup_org_2022_field_dimensions_schema_json(data):
    if not isinstance(data, (dict)):
        raise ValueError("data must be object")
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_len = len(data)
        if not all(prop in data for prop in ['field', 'goal']):
            raise ValueError("data must contain ['field', 'goal'] properties")
        data_keys = set(data.keys())
        if "field" in data_keys:
            data_keys.remove("field")
            data__field = data["field"]
            if not isinstance(data__field, (dict)):
                raise ValueError("data.field must be object")
            data__field_is_dict = isinstance(data__field, dict)
            if data__field_is_dict:
                data__field_len = len(data__field)
                if not all(prop in data__field for prop in ['length', 'width', 'lineWidth', 'penaltyMarkSize', 'penaltyAreaLength', 'penaltyAreaWidth', 'penaltyMarkDistance', 'centerCircleDiameter', 'borderStripWidth']):
                    raise ValueError("data.field must contain ['length', 'width', 'lineWidth', 'penaltyMarkSize', 'penaltyAreaLength', 'penaltyAreaWidth', 'penaltyMarkDistance', 'centerCircleDiameter', 'borderStripWidth'] properties")
                data__field_keys = set(data__field.keys())
                if "length" in data__field_keys:
                    data__field_keys.remove("length")
                    data__field__length = data__field["length"]
                    if not isinstance(data__field__length, (int, float)) or isinstance(data__field__length, bool):
                        raise ValueError("data.field.length must be number")
                    if isinstance(data__field__length, (int, float)):
                        if data__field__length < 3:
                            raise ValueError("data.field.length must be bigger than or equal to 3")
                        if data__field__length > 20:
                            raise ValueError("data.field.length must be smaller than or equal to 20")
                if "width" in data__field_keys:
                    data__field_keys.remove("width")
                    data__field__width = data__field["width"]
                    if not isinstance(data__field__width, (int, float)) or isinstance(data__field__width, bool):
                        raise ValueError("data.field.width must be number")
                    if isinstance(data__field__width, (int, float)):
                        if data__field__width < 3:
                            raise ValueError("data.field.width must be bigger than or equal to 3")
                        if data__field__width > 20:
                            raise ValueError("data.field.width must be smaller than or equal to 20")
                if "lineWidth" in data__field_keys:
                    data__field_keys.remove("lineWidth")
                    data__field__lineWidth = data__field["lineWidth"]
                    if not isinstance(data__field__lineWidth, (int, float)) or isinstance(data__field__lineWidth, bool):
                        raise ValueError("data.field.lineWidth must be number")
                    if isinstance(data__field__lineWidth, (int, float)):
                        if data__field__lineWidth < 0.05:
                            raise ValueError("data.field.lineWidth must be bigger than or equal to 0.05")
                        if data__field__lineWidth > 0.05:
                            raise ValueError("data.field.lineWidth must be smaller than or equal to 0.05")
                if "penaltyMarkSize" in data__field_keys:
                    data__field_keys.remove("penaltyMarkSize")
                    data__field__penaltyMarkSize = data__field["penaltyMarkSize"]
                    if not isinstance(data__field__penaltyMarkSize, (int, float)) or isinstance(data__field__penaltyMarkSize, bool):
                        raise ValueError("data.field.penaltyMarkSize must be number")
                    if isinstance(data__field__penaltyMarkSize, (int, float)):
                        if data__field__penaltyMarkSize < 0.01:
                            raise ValueError("data.field.penaltyMarkSize must be bigger than or equal to 0.01")
                        if data__field__penaltyMarkSize > 5:
                            raise ValueError("data.field.penaltyMarkSize must be smaller than or equal to 5")
                if "goalAreaLength" in data__field_keys:
                    data__field_keys.remove("goalAreaLength")
                    data__field__goalAreaLength = data__field["goalAreaLength"]
                    if not isinstance(data__field__goalAreaLength, (int, float)) or isinstance(data__field__goalAreaLength, bool):
                        raise ValueError("data.field.goalAreaLength must be number")
                    if isinstance(data__field__goalAreaLength, (int, float)):
                        if data__field__goalAreaLength < 0.3:
                            raise ValueError("data.field.goalAreaLength must be bigger than or equal to 0.3")
                        if data__field__goalAreaLength > 10:
                            raise ValueError("data.field.goalAreaLength must be smaller than or equal to 10")
                if "goalAreaWidth" in data__field_keys:
                    data__field_keys.remove("goalAreaWidth")
                    data__field__goalAreaWidth = data__field["goalAreaWidth"]
                    if not isinstance(data__field__goalAreaWidth, (int, float)) or isinstance(data__field__goalAreaWidth, bool):
                        raise ValueError("data.field.goalAreaWidth must be number")
                    if isinstance(data__field__goalAreaWidth, (int, float)):
                        if data__field__goalAreaWidth < 1:
                            raise ValueError("data.field.goalAreaWidth must be bigger than or equal to 1")
                        if data__field__goalAreaWidth > 10:
                            raise ValueError("data.field.goalAreaWidth must be smaller than or equal to 10")
                if "penaltyAreaLength" in data__field_keys:
                    data__field_keys.remove("penaltyAreaLength")
                    data__field__penaltyAreaLength = data__field["penaltyAreaLength"]
                    if not isinstance(data__field__penaltyAreaLength, (int, float)) or isinstance(data__field__penaltyAreaLength, bool):
                        raise ValueError("data.field.penaltyAreaLength must be number")
                    if isinstance(data__field__penaltyAreaLength, (int, float)):
                        if data__field__penaltyAreaLength < 0.3:
                            raise ValueError("data.field.penaltyAreaLength must be bigger than or equal to 0.3")
                        if data__field__penaltyAreaLength > 10:
                            raise ValueError("data.field.penaltyAreaLength must be smaller than or equal to 10")
                if "penaltyAreaWidth" in data__field_keys:
                    data__field_keys.remove("penaltyAreaWidth")
                    data__field__penaltyAreaWidth = data__field["penaltyAreaWidth"]
                    if not isinstance(data__field__penaltyAreaWidth, (int, float)) or isinstance(data__field__penaltyAreaWidth, bool):
                        raise ValueError("data.field.penaltyAreaWidth must be number")
                    if isinstance(data__field__penaltyAreaWidth, (int, float)):
                        if data__field__penaltyAreaWidth < 1:
                            raise ValueError("data.field.penaltyAreaWidth must be bigger than or equal to 1")
                        if data__field__penaltyAreaWidth > 10:
                            raise ValueError("data.field.penaltyAreaWidth must be smaller than or equal to 10")
                if "penaltyMarkDistance" in data__field_keys:
                    data__field_keys.remove("penaltyMarkDistance")
                    data__field__penaltyMarkDistance = data__field["penaltyMarkDistance"]
                    if not isinstance(data__field__penaltyMarkDistance, (int, float)) or isinstance(data__field__penaltyMarkDistance, bool):
                        raise ValueError("data.field.penaltyMarkDistance must be number")
                    if isinstance(data__field__penaltyMarkDistance, (int, float)):
                        if data__field__penaltyMarkDistance < 0.3:
                            raise ValueError("data.field.penaltyMarkDistance must be bigger than or equal to 0.3")
                        if data__field__penaltyMarkDistance > 10:
                            raise ValueError("data.field.penaltyMarkDistance must be smaller than or equal to 10")
                if "centerCircleDiameter" in data__field_keys:
                    data__field_keys.remove("centerCircleDiameter")
                    data__field__centerCircleDiameter = data__field["centerCircleDiameter"]
                    if not isinstance(data__field__centerCircleDiameter, (int, float)) or isinstance(data__field__centerCircleDiameter, bool):
                        raise ValueError("data.field.centerCircleDiameter must be number")
                    if isinstance(data__field__centerCircleDiameter, (int, float)):
                        if data__field__centerCircleDiameter < 0.3:
                            raise ValueError("data.field.centerCircleDiameter must be bigger than or equal to 0.3")
                        if data__field__centerCircleDiameter > 10:
                            raise ValueError("data.field.centerCircleDiameter must be smaller than or equal to 10")
                if "borderStripWidth" in data__field_keys:
                    data__field_keys.remove("borderStripWidth")
                    data__field__borderStripWidth = data__field["borderStripWidth"]
                    if not isinstance(data__field__borderStripWidth, (int, float)) or isinstance(data__field__borderStripWidth, bool):
                        raise ValueError("data.field.borderStripWidth must be number")
                    if isinstance(data__field__borderStripWidth, (int, float)):
                        if data__field__borderStripWidth < 0.2:
                            raise ValueError("data.field.borderStripWidth must be bigger than or equal to 0.2")
                        if data__field__borderStripWidth > 2:
                            raise ValueError("data.field.borderStripWidth must be smaller than or equal to 2")
        if "goal" in data_keys:
            data_keys.remove("goal")
            data__goal = data["goal"]
            if not isinstance(data__goal, (dict)):
                raise ValueError("data.goal must be object")
            data__goal_is_dict = isinstance(data__goal, dict)
            if data__goal_is_dict:
                data__goal_len = len(data__goal)
                if not all(prop in data__goal for prop in ['postDiameter', 'height', 'innerWidth', 'depth']):
                    raise ValueError("data.goal must contain ['postDiameter', 'height', 'innerWidth', 'depth'] properties")
                data__goal_keys = set(data__goal.keys())
                if "postDiameter" in data__goal_keys:
                    data__goal_keys.remove("postDiameter")
                    data__goal__postDiameter = data__goal["postDiameter"]
                    if not isinstance(data__goal__postDiameter, (int, float)) or isinstance(data__goal__postDiameter, bool):
                        raise ValueError("data.goal.postDiameter must be number")
                    if isinstance(data__goal__postDiameter, (int, float)):
                        if data__goal__postDiameter < 0.01:
                            raise ValueError("data.goal.postDiameter must be bigger than or equal to 0.01")
                        if data__goal__postDiameter > 4:
                            raise ValueError("data.goal.postDiameter must be smaller than or equal to 4")
                if "height" in data__goal_keys:
                    data__goal_keys.remove("height")
                    data__goal__height = data__goal["height"]
                    if not isinstance(data__goal__height, (int, float)) or isinstance(data__goal__height, bool):
                        raise ValueError("data.goal.height must be number")
                    if isinstance(data__goal__height, (int, float)):
                        if data__goal__height < 0.3:
                            raise ValueError("data.goal.height must be bigger than or equal to 0.3")
                        if data__goal__height > 10:
                            raise ValueError("data.goal.height must be smaller than or equal to 10")
                if "innerWidth" in data__goal_keys:
                    data__goal_keys.remove("innerWidth")
                    data__goal__innerWidth = data__goal["innerWidth"]
                    if not isinstance(data__goal__innerWidth, (int, float)) or isinstance(data__goal__innerWidth, bool):
                        raise ValueError("data.goal.innerWidth must be number")
                    if isinstance(data__goal__innerWidth, (int, float)):
                        if data__goal__innerWidth < 0.3:
                            raise ValueError("data.goal.innerWidth must be bigger than or equal to 0.3")
                        if data__goal__innerWidth > 10:
                            raise ValueError("data.goal.innerWidth must be smaller than or equal to 10")
                if "depth" in data__goal_keys:
                    data__goal_keys.remove("depth")
                    data__goal__depth = data__goal["depth"]
                    if not isinstance(data__goal__depth, (int, float)) or isinstance(data__goal__depth, bool):
                        raise ValueError("data.goal.depth must be number")
                    if isinstance(data__goal__depth, (int, float)):
                        if data__goal__depth < 0.3:
                            raise ValueError("data.goal.depth must be bigger than or equal to 0.3")
                        if data__goal__depth > 10:
                            raise ValueError("data.goal.depth must be smaller than or equal to 10")
    return data
