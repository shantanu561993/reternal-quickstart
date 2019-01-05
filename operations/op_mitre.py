from operations.models import Mitre as MitreDB
import mongoengine

class Mitre:
    def create(name, technique_id, description, platforms, permissions_required, data_sources, references, killchain):
        try:
            mitre_object = MitreDB(
                        name = name,
                        technique_id = technique_id,
                        description = description,
                        platforms = platforms,
                        permissions_required = permissions_required,
                        data_sources = data_sources,
                        references = references,
                        kill_chain_phases = killchain
                    ).save()
                    
            result = {"result":"success", "message":"Succesfully added Mitre technique to DB"}

        except mongoengine.errors.NotUniqueError:
            result = {"result":"failed", "message":"Mitre technique already exists"}


        except Exception as err:
            result = {"result":"failed", "message":"Error importing Mitre technique"}

        return result