VERSION = "2.15.1"


NoneType = type(None)

def validate_https___spl_robocup_org_2021_field_dimensions_schema_json(data):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object")
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_len = len(data)
        if not all(prop in data for prop in ['field', 'goal']):
            raise JsonSchemaValueException("data must contain ['field', 'goal'] properties")
        data_keys = set(data.keys())
        if "field" in data_keys:
            data_keys.remove("field")
            data__field = data["field"]
            if not isinstance(data__field, (dict)):
                raise JsonSchemaValueException("data.field must be object")
            data__field_is_dict = isinstance(data__field, dict)
            if data__field_is_dict:
                data__field_len = len(data__field)
                if not all(prop in data__field for prop in ['length', 'width', 'lineWidth', 'penaltyMarkerSize', 'penaltyAreaLength', 'penaltyAreaWidth', 'penaltyCrossDistance', 'centerCircleDiameter', 'borderStripWidth']):
                    raise JsonSchemaValueException("data.field must contain ['length', 'width', 'lineWidth', 'penaltyMarkerSize', 'penaltyAreaLength', 'penaltyAreaWidth', 'penaltyCrossDistance', 'centerCircleDiameter', 'borderStripWidth'] properties")
                data__field_keys = set(data__field.keys())
                if "length" in data__field_keys:
                    data__field_keys.remove("length")
                    data__field__length = data__field["length"]
                    if not isinstance(data__field__length, (int, float)) or isinstance(data__field__length, bool):
                        raise JsonSchemaValueException("data.field.length must be number")
                    if isinstance(data__field__length, (int, float)):
                        if data__field__length < 3:
                            raise JsonSchemaValueException("data.field.length must be bigger than or equal to 3")
                        if data__field__length > 20:
                            raise JsonSchemaValueException("data.field.length must be smaller than or equal to 20")
                if "width" in data__field_keys:
                    data__field_keys.remove("width")
                    data__field__width = data__field["width"]
                    if not isinstance(data__field__width, (int, float)) or isinstance(data__field__width, bool):
                        raise JsonSchemaValueException("data.field.width must be number")
                    if isinstance(data__field__width, (int, float)):
                        if data__field__width < 3:
                            raise JsonSchemaValueException("data.field.width must be bigger than or equal to 3")
                        if data__field__width > 20:
                            raise JsonSchemaValueException("data.field.width must be smaller than or equal to 20")
                if "lineWidth" in data__field_keys:
                    data__field_keys.remove("lineWidth")
                    data__field__lineWidth = data__field["lineWidth"]
                    if not isinstance(data__field__lineWidth, (int, float)) or isinstance(data__field__lineWidth, bool):
                        raise JsonSchemaValueException("data.field.lineWidth must be number")
                    if isinstance(data__field__lineWidth, (int, float)):
                        if data__field__lineWidth < 0.01:
                            raise JsonSchemaValueException("data.field.lineWidth must be bigger than or equal to 0.01")
                        if data__field__lineWidth > 5:
                            raise JsonSchemaValueException("data.field.lineWidth must be smaller than or equal to 5")
                if "penaltyMarkerSize" in data__field_keys:
                    data__field_keys.remove("penaltyMarkerSize")
                    data__field__penaltyMarkerSize = data__field["penaltyMarkerSize"]
                    if not isinstance(data__field__penaltyMarkerSize, (int, float)) or isinstance(data__field__penaltyMarkerSize, bool):
                        raise JsonSchemaValueException("data.field.penaltyMarkerSize must be number")
                    if isinstance(data__field__penaltyMarkerSize, (int, float)):
                        if data__field__penaltyMarkerSize < 0.01:
                            raise JsonSchemaValueException("data.field.penaltyMarkerSize must be bigger than or equal to 0.01")
                        if data__field__penaltyMarkerSize > 5:
                            raise JsonSchemaValueException("data.field.penaltyMarkerSize must be smaller than or equal to 5")
                if "goalBoxAreaLength" in data__field_keys:
                    data__field_keys.remove("goalBoxAreaLength")
                    data__field__goalBoxAreaLength = data__field["goalBoxAreaLength"]
                    if not isinstance(data__field__goalBoxAreaLength, (int, float)) or isinstance(data__field__goalBoxAreaLength, bool):
                        raise JsonSchemaValueException("data.field.goalBoxAreaLength must be number")
                    if isinstance(data__field__goalBoxAreaLength, (int, float)):
                        if data__field__goalBoxAreaLength < 0.3:
                            raise JsonSchemaValueException("data.field.goalBoxAreaLength must be bigger than or equal to 0.3")
                        if data__field__goalBoxAreaLength > 10:
                            raise JsonSchemaValueException("data.field.goalBoxAreaLength must be smaller than or equal to 10")
                if "goalBoxAreaWidth" in data__field_keys:
                    data__field_keys.remove("goalBoxAreaWidth")
                    data__field__goalBoxAreaWidth = data__field["goalBoxAreaWidth"]
                    if not isinstance(data__field__goalBoxAreaWidth, (int, float)) or isinstance(data__field__goalBoxAreaWidth, bool):
                        raise JsonSchemaValueException("data.field.goalBoxAreaWidth must be number")
                    if isinstance(data__field__goalBoxAreaWidth, (int, float)):
                        if data__field__goalBoxAreaWidth < 1:
                            raise JsonSchemaValueException("data.field.goalBoxAreaWidth must be bigger than or equal to 1")
                        if data__field__goalBoxAreaWidth > 10:
                            raise JsonSchemaValueException("data.field.goalBoxAreaWidth must be smaller than or equal to 10")
                if "penaltyAreaLength" in data__field_keys:
                    data__field_keys.remove("penaltyAreaLength")
                    data__field__penaltyAreaLength = data__field["penaltyAreaLength"]
                    if not isinstance(data__field__penaltyAreaLength, (int, float)) or isinstance(data__field__penaltyAreaLength, bool):
                        raise JsonSchemaValueException("data.field.penaltyAreaLength must be number")
                    if isinstance(data__field__penaltyAreaLength, (int, float)):
                        if data__field__penaltyAreaLength < 0.3:
                            raise JsonSchemaValueException("data.field.penaltyAreaLength must be bigger than or equal to 0.3")
                        if data__field__penaltyAreaLength > 10:
                            raise JsonSchemaValueException("data.field.penaltyAreaLength must be smaller than or equal to 10")
                if "penaltyAreaWidth" in data__field_keys:
                    data__field_keys.remove("penaltyAreaWidth")
                    data__field__penaltyAreaWidth = data__field["penaltyAreaWidth"]
                    if not isinstance(data__field__penaltyAreaWidth, (int, float)) or isinstance(data__field__penaltyAreaWidth, bool):
                        raise JsonSchemaValueException("data.field.penaltyAreaWidth must be number")
                    if isinstance(data__field__penaltyAreaWidth, (int, float)):
                        if data__field__penaltyAreaWidth < 1:
                            raise JsonSchemaValueException("data.field.penaltyAreaWidth must be bigger than or equal to 1")
                        if data__field__penaltyAreaWidth > 10:
                            raise JsonSchemaValueException("data.field.penaltyAreaWidth must be smaller than or equal to 10")
                if "penaltyCrossDistance" in data__field_keys:
                    data__field_keys.remove("penaltyCrossDistance")
                    data__field__penaltyCrossDistance = data__field["penaltyCrossDistance"]
                    if not isinstance(data__field__penaltyCrossDistance, (int, float)) or isinstance(data__field__penaltyCrossDistance, bool):
                        raise JsonSchemaValueException("data.field.penaltyCrossDistance must be number")
                    if isinstance(data__field__penaltyCrossDistance, (int, float)):
                        if data__field__penaltyCrossDistance < 0.3:
                            raise JsonSchemaValueException("data.field.penaltyCrossDistance must be bigger than or equal to 0.3")
                        if data__field__penaltyCrossDistance > 10:
                            raise JsonSchemaValueException("data.field.penaltyCrossDistance must be smaller than or equal to 10")
                if "centerCircleDiameter" in data__field_keys:
                    data__field_keys.remove("centerCircleDiameter")
                    data__field__centerCircleDiameter = data__field["centerCircleDiameter"]
                    if not isinstance(data__field__centerCircleDiameter, (int, float)) or isinstance(data__field__centerCircleDiameter, bool):
                        raise JsonSchemaValueException("data.field.centerCircleDiameter must be number")
                    if isinstance(data__field__centerCircleDiameter, (int, float)):
                        if data__field__centerCircleDiameter < 0.3:
                            raise JsonSchemaValueException("data.field.centerCircleDiameter must be bigger than or equal to 0.3")
                        if data__field__centerCircleDiameter > 10:
                            raise JsonSchemaValueException("data.field.centerCircleDiameter must be smaller than or equal to 10")
                if "borderStripWidth" in data__field_keys:
                    data__field_keys.remove("borderStripWidth")
                    data__field__borderStripWidth = data__field["borderStripWidth"]
                    if not isinstance(data__field__borderStripWidth, (int, float)) or isinstance(data__field__borderStripWidth, bool):
                        raise JsonSchemaValueException("data.field.borderStripWidth must be number")
                    if isinstance(data__field__borderStripWidth, (int, float)):
                        if data__field__borderStripWidth < 0.1:
                            raise JsonSchemaValueException("data.field.borderStripWidth must be bigger than or equal to 0.1")
                        if data__field__borderStripWidth > 1000:
                            raise JsonSchemaValueException("data.field.borderStripWidth must be smaller than or equal to 1000")
        if "goal" in data_keys:
            data_keys.remove("goal")
            data__goal = data["goal"]
            if not isinstance(data__goal, (dict)):
                raise JsonSchemaValueException("data.goal must be object")
            data__goal_is_dict = isinstance(data__goal, dict)
            if data__goal_is_dict:
                data__goal_len = len(data__goal)
                if not all(prop in data__goal for prop in ['postDiameter', 'height', 'innerWidth', 'depth']):
                    raise JsonSchemaValueException("data.goal must contain ['postDiameter', 'height', 'innerWidth', 'depth'] properties")
                data__goal_keys = set(data__goal.keys())
                if "postDiameter" in data__goal_keys:
                    data__goal_keys.remove("postDiameter")
                    data__goal__postDiameter = data__goal["postDiameter"]
                    if not isinstance(data__goal__postDiameter, (int, float)) or isinstance(data__goal__postDiameter, bool):
                        raise JsonSchemaValueException("data.goal.postDiameter must be number")
                    if isinstance(data__goal__postDiameter, (int, float)):
                        if data__goal__postDiameter < 0.01:
                            raise JsonSchemaValueException("data.goal.postDiameter must be bigger than or equal to 0.01")
                        if data__goal__postDiameter > 4:
                            raise JsonSchemaValueException("data.goal.postDiameter must be smaller than or equal to 4")
                if "height" in data__goal_keys:
                    data__goal_keys.remove("height")
                    data__goal__height = data__goal["height"]
                    if not isinstance(data__goal__height, (int, float)) or isinstance(data__goal__height, bool):
                        raise JsonSchemaValueException("data.goal.height must be number")
                    if isinstance(data__goal__height, (int, float)):
                        if data__goal__height < 0.3:
                            raise JsonSchemaValueException("data.goal.height must be bigger than or equal to 0.3")
                        if data__goal__height > 10:
                            raise JsonSchemaValueException("data.goal.height must be smaller than or equal to 10")
                if "innerWidth" in data__goal_keys:
                    data__goal_keys.remove("innerWidth")
                    data__goal__innerWidth = data__goal["innerWidth"]
                    if not isinstance(data__goal__innerWidth, (int, float)) or isinstance(data__goal__innerWidth, bool):
                        raise JsonSchemaValueException("data.goal.innerWidth must be number")
                    if isinstance(data__goal__innerWidth, (int, float)):
                        if data__goal__innerWidth < 0.3:
                            raise JsonSchemaValueException("data.goal.innerWidth must be bigger than or equal to 0.3")
                        if data__goal__innerWidth > 10:
                            raise JsonSchemaValueException("data.goal.innerWidth must be smaller than or equal to 10")
                if "depth" in data__goal_keys:
                    data__goal_keys.remove("depth")
                    data__goal__depth = data__goal["depth"]
                    if not isinstance(data__goal__depth, (int, float)) or isinstance(data__goal__depth, bool):
                        raise JsonSchemaValueException("data.goal.depth must be number")
                    if isinstance(data__goal__depth, (int, float)):
                        if data__goal__depth < 0.3:
                            raise JsonSchemaValueException("data.goal.depth must be bigger than or equal to 0.3")
                        if data__goal__depth > 10:
                            raise JsonSchemaValueException("data.goal.depth must be smaller than or equal to 10")
    return data
