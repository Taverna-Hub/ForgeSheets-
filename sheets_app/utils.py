from os import error
from .models import Equipment, Sheet, Race
import re
def sheet_update(name, strength, intelligence, wisdom, charisma, constitution, speed, healthPoint, healthPointMax, manaActual, manaMax, exp, expActual, expMax):
    errors = []
    print("itils= ", healthPoint, manaActual, exp)
    # Tratando nomes!
    if str(name).count(' ') == len(name):
        errors.append({
            'field': 'name',
            'message' : 'Este campo não pode ser vazio!'
            })
    elif 2 > len(name) or len(name) > 50:
        errors.append({
            'field':'name',
            'message': 'Insira de 2 a 50 caracteres!'
            })
        
    # Tratando Atributos    
    if str(strength).count(' ') == len(str(strength)) or str(intelligence).count(' ') == len(str(intelligence)) or str(wisdom).count(' ') == len(str(wisdom)) or str(charisma).count(' ') == len(str(charisma)) or str(constitution).count(' ') == len(str(constitution)) or str(speed).count(' ') == len(str(speed)):
        errors.append({
            'field': 'atributes1',
            'message' : 'Este(s) campo(s) não pode(m) ser vazio(s)!'
            })
        if str(strength).count(' ') == len(str(strength)):
            errors.append("strength")
        if str(intelligence).count(' ') == len(str(intelligence)):
            errors.append("intelligence")
        if str(charisma).count(' ') == len(str(charisma)):
            errors.append("charisma")
        if str(speed).count(' ') == len(str(speed)):
            errors.append("speed")
        if str(wisdom).count(' ') == len(str(wisdom)):
            errors.append("wisdom")
        if str(constitution).count(' ') == len(str(constitution)):
            errors.append("constitution")

    elif int(strength) < 1 or int(intelligence) < 1 or int(wisdom) < 1 or int(charisma) < 1 or int(constitution) < 1 or int(speed) < 1:
        errors.append({
            'field' : 'atributes1',
            'message' : 'O atributo deve ser no minímo 1'
            })
        if int(strength) < 1:
            errors.append("strength")
        if int(intelligence) < 1:
            errors.append("intelligence")
        if int(wisdom) < 1 :
            errors.append("wisdom")
        if int(speed) < 1:
            errors.append("speed")
        if int(charisma) < 1 :
            errors.append("charisma")
        if int(constitution) < 1:
            errors.append("constitution")

    elif atribute_verifier(str(strength)) == 1 or atribute_verifier(str(intelligence)) == 1 or atribute_verifier(str(wisdom)) == 1 or atribute_verifier(str(charisma)) == 1 or atribute_verifier(str(constitution)) == 1 or atribute_verifier(str(speed)) == 1:
        errors.append({
            'field' : 'atributes1',
            'message' : 'Os atributos primarios devem ser numeros inteiros'
            })
        if atribute_verifier(str(strength)) == 1:
            errors.append("strength")
        if atribute_verifier(str(intelligence)) == 1:
            errors.append("intelligence")
        if atribute_verifier(str(wisdom)) == 1:
            errors.append("wisdom")
        if atribute_verifier(str(speed)) == 1:
            errors.append("speed")
        if  atribute_verifier(str(charisma)) == 1:
            errors.append("charisma")
        if  atribute_verifier(str(constitution)) == 1:
            errors.append("constitution")
    
    if str(healthPoint).count(' ') == len(str(healthPoint)) or str(exp).count(' ') == len(str(exp)) or str(manaActual).count(' ') == len(str(manaActual)):
        print('if = ', healthPoint, exp, manaActual)
        errors.append({
            'field': 'atributes2',
            'message' : 'Estes campos não podem ser vazios'
            })
        if str(healthPointMax).count(' ') == len(str(healthPointMax)):
            errors.append("healthPointMax")
        if str(manaMax).count(' ') == len(str(manaMax)):
            errors.append("manaMax")
        if str(exp).count(' ') == len(str(exp)):
            errors.append("exp")
    
    elif atribute_verifier(str(healthPointMax)) == 1 or atribute_verifier(str(manaMax)) == 1 or atribute_verifier(str(exp)) == 1:
        errors.append({
            'field' : 'atributes2',
            'message' : 'Os atributos secundarios devem ser numeros inteiros'
            })
        if atribute_verifier(str(healthPointMax)) == 1:
            errors.append("healthPointMax")
        if atribute_verifier(str(manaMax)) == 1:
            errors.append("manaMax")
        if atribute_verifier(str(exp)) == 1:
            errors.append("exp")

    elif int(healthPointMax) < 1 or int(manaMax) < 1 or int(healthPointMax) > 100000 or int(manaMax) > 100000:
        errors.append({
            'field' : 'atributes2',
            'message' : 'Vida e mana não podem ser menores que 1 ou maiores que 100 mil'
            })
        if int(healthPointMax) < 1 or int(healthPointMax) > 100000:
            errors.append("healthPointMax")
        if int(manaMax) < 1 or int(manaMax) > 100000:
            errors.append("manaMax")
    elif int(exp) < 0 or int(exp) > 105000000:
        errors.append({
            'field' : 'atributes2',
            'message' : 'A experiência não pode ser menor que 0 ou maior que 105M'
            })
        errors.append("exp")

    elif int(exp) < int(expActual):
        errors.append({
            'field': 'atributes2',
            'message': 'Você somente pode adicionar experiência!'
        })
    if len(errors) > 0:
        return errors
    
    sheet_updated = Sheet(name = name, strength = strength, intelligence = intelligence, wisdom = wisdom, charisma = charisma, constitution = constitution, speed = speed, healthPointMax = healthPointMax, manaMax = manaMax, exp = exp, expTotal = exp, expMax = expMax, healthPoint = healthPointMax, mana = manaMax)
    # sheet_updated.save()
    # sheet_updated.updateXp()
    # sheet_updated.save()
    return sheet_updated


#Tratamento de erro na utils
def save_equipment(name, quantity, attack, defense, equipment):
    name_treated = name.strip()
    quantity_treated = int(quantity)
    attack_treated = int(attack)
    defense_treated = int(defense)
    wrong_fields = []

    if not name_treated:
        wrong_fields.append({
            'field': 'name',
            'message': 'Este campo não pode ser vazio'
        })
    elif len(name) > 55:
        wrong_fields.append({
            'field': 'name',
            'message': 'Este campo deve ter menos de 55 caractéres'
        })
    elif len(name) < 2:
        wrong_fields.append({
            'field': 'name',
            'message': 'Este campo deve ter mais de 2 caractéres'
        })
    if quantity_treated < 1:
        wrong_fields.append({
            'field': 'quantity',
            'message': 'A quantidade não pode ser inferior a 1'
        })   
    if attack_treated < 0:
        wrong_fields.append({
            'field': 'attack',
            'message': 'O valor de ataque não pode ser inferior a 0'
        })
    if defense_treated < 0:
        wrong_fields.append({
            'field': 'defense',
            'message': 'O valor de defesa não pode ser inferior a 0'
        })

    if type(quantity) != int:
        wrong_fields.append({
            'field': 'quantity',
            'message': 'Utilize apenas números inteiros'
        })
    if type(attack) != int:
        wrong_fields.append({
            'field': 'attack',
            'message': 'Utilize apenas números inteiros'
        })

    if type(defense) != int:
        wrong_fields.append({
            'field': 'defense',
            'message': 'Utilize apenas números inteiros'
        })

    if len(wrong_fields) > 0:
        return wrong_fields
    
    equipment.name = name
    equipment.quantity = quantity
    equipment.attack = attack
    equipment.defense = defense
    equipment.save()


def atribute_verifier(atr):
    return 1 if not re.match(r'^[-+]?\d*\.?\d+$', atr) else 0

# add imagem
def save_sheet(name, race, role, image, strength, intelligence, wisdom, charisma, constitution, speed, healthPointMax, manaMax, exp, user_id, description):
    errors=[]

    image_treated = re.match(r'^(?:https?|ftp):\/\/(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:\/[^\s?]*)?(?:\?[^\s]*)?$', image)
    if image != '':
        if not image_treated:
            errors.append({
                'field': 'image',
                'message': 'Insira uma URL válida!'
            })
        elif len(str(image)) > 200:
            errors.append({
                    'field': 'image',
                    'message': 'A URL deve ter no maximo 200 caracteres!'
                })

    if str(name).count(' ') == len(name):
        errors.append({
            'field': 'name',
            'message' : 'Este campo não pode ser vazio!'
            })
    elif 2 > len(name) or len(name) > 50:
        errors.append({
            'field':'name',
            'message': 'Insira de 2 a 50 caracteres!'
            })
    if str(race).count(' ') == len(str(race)):
        errors.append({
            'field': 'race',
            'message' : 'Este campo não pode ser vazio!'
            })
    elif 2 > len(race) or len(race) > 22:
        errors.append({
            'field': 'race',
            'message': 'Insira de 2 a 22 caracteres!'
        })
    if str(role).count(' ') == len(str(role)):
        errors.append({
            'field': 'role',
            'message' : 'Este campo não pode ser vazio!'
            })
    if 2 > len(role) or len(role) > 22:
        errors.append({
            'field': 'role',
            'message': 'Insira de 2 a 22 caracteres!'
        })
        
    if str(strength).count(' ') == len(str(strength)) or str(intelligence).count(' ') == len(str(intelligence)) or str(wisdom).count(' ') == len(str(wisdom)) or str(charisma).count(' ') == len(str(charisma)) or str(constitution).count(' ') == len(str(constitution)) or str(speed).count(' ') == len(str(speed)):
        errors.append({
            'field': 'atributes1',
            'message' : 'Este(s) campo(s) não pode(m) ser vazio(s)!'
            })
        if str(strength).count(' ') == len(str(strength)):
            errors.append("strength")
        if str(intelligence).count(' ') == len(str(intelligence)):
            errors.append("intelligence")
        if str(charisma).count(' ') == len(str(charisma)):
            errors.append("charisma")
        if str(speed).count(' ') == len(str(speed)):
            errors.append("speed")
        if str(wisdom).count(' ') == len(str(wisdom)):
            errors.append("wisdom")
        if str(constitution).count(' ') == len(str(constitution)):
            errors.append("constitution")

    elif 20 < int(strength) or int(strength) < 1 or 20 < int(intelligence) or int(intelligence) < 1 or 20 < int(wisdom) or int(wisdom) < 1 or 20 < int(charisma) or int(charisma) < 1 or 20 < int(constitution) or int(constitution) < 1 or 20 < int(speed) or int(speed) < 1:
        errors.append({
            'field' : 'atributes1',
            'message' : 'Os atributos devem estar entre 1 e 20'
            })
        if 20 < int(strength) or int(strength) < 1:
            errors.append("strength")
        if 20 < int(intelligence) or int(intelligence) < 1:
            errors.append("intelligence")
        if 20 < int(wisdom) or int(wisdom) < 1 :
            errors.append("wisdom")
        if 20 < int(speed) or int(speed) < 1:
            errors.append("speed")
        if  20 < int(charisma) or int(charisma) < 1 :
            errors.append("charisma")
        if  20 < int(constitution) or int(constitution) < 1:
            errors.append("constitution")

    elif atribute_verifier(str(strength)) == 1 or atribute_verifier(str(intelligence)) == 1 or atribute_verifier(str(wisdom)) == 1 or atribute_verifier(str(charisma)) == 1 or atribute_verifier(str(constitution)) == 1 or atribute_verifier(str(speed)) == 1:
        errors.append({
            'field' : 'atributes1',
            'message' : 'Os atributos primarios devem ser numeros inteiros'
            })
        if atribute_verifier(str(strength)) == 1:
            errors.append("strength")
        if atribute_verifier(str(intelligence)) == 1:
            errors.append("intelligence")
        if atribute_verifier(str(wisdom)) == 1:
            errors.append("wisdom")
        if atribute_verifier(str(speed)) == 1:
            errors.append("speed")
        if  atribute_verifier(str(charisma)) == 1:
            errors.append("charisma")
        if  atribute_verifier(str(constitution)) == 1:
            errors.append("constitution")

    if str(healthPointMax).count(' ') == len(str(healthPointMax)) or str(exp).count(' ') == len(str(exp)) or str(manaMax).count(' ') == len(str(manaMax)):
        errors.append({
            'field': 'atributes2',
            'message' : 'Estes campos não podem ser vazios'
            })
        if str(healthPointMax).count(' ') == len(str(healthPointMax)):
            errors.append("healthPointMax")
        if str(manaMax).count(' ') == len(str(manaMax)):
            errors.append("manaMax")
        if str(exp).count(' ') == len(str(exp)):
            errors.append("exp")

    elif atribute_verifier(str(healthPointMax)) == 1 or atribute_verifier(str(manaMax)) == 1 or atribute_verifier(str(exp)) == 1:
        errors.append({
            'field' : 'atributes2',
            'message' : 'Os atributos secundarios devem ser numeros inteiros'
            })
        if atribute_verifier(str(healthPointMax)) == 1:
            errors.append("healthPointMax")
        if atribute_verifier(str(manaMax)) == 1:
            errors.append("manaMax")
        if atribute_verifier(str(exp)) == 1:
            errors.append("exp")

    elif int(healthPointMax) < 1 or int(manaMax) < 1 or int(healthPointMax) > 100000 or int(manaMax) > 100000:
        errors.append({
            'field' : 'atributes2',
            'message' : 'Vida e mana não podem ser menores que 1 ou maiores que 100 mil'
            })
        if int(healthPointMax) < 1 or int(healthPointMax) > 100000:
            errors.append("healthPointMax")
        if int(manaMax) < 1 or int(manaMax) > 100000:
            errors.append("manaMax")

    elif int(exp) < 0 or int(exp) > 105000000:
        errors.append({
            'field' : 'atributes2',
            'message' : 'A experiência não pode ser menor que 0 ou maior que 105M'
            })
        errors.append("exp")
        
    if len(errors) > 0:
        return errors
    #add imagem
    sheet = Sheet(name = name, race = race, role = role, image = image, strength = strength, intelligence = intelligence, wisdom = wisdom, charisma = charisma, constitution = constitution, speed = speed, healthPointMax = healthPointMax, manaMax = manaMax, exp = exp, expTotal = exp, healthPoint = healthPointMax, mana = manaMax, user_id = user_id, description = description)
    sheet.save()
    sheet.updateXp()
    sheet.save()
    return sheet
