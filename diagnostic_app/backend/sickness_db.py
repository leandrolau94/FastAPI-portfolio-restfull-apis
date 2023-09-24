from pydantic import BaseModel

class Sickness(BaseModel):
    id: int
    name: str
    symptoms: str
    causes: str
    treatment: str

arrOfdiseases : list[Sickness] = [
    {
        "id": 1,
        "name": "Acalasia",
        "symptoms": "Incapacidad para tragar(disfagia). Regurgitacion de comida o saliva. Acidez estomacal. Eructacion. Dolor en el pecho que aparece y desaparece. Tos nocturna. Neumonia. Perdida de peso. Vomitos",
        "causes": "La causa exacta de la Acalasia no se entiende bien. Los investigadores sospechan que puede ser causada por una perdida de celulas nerviosas en el esofago. Hay teorias sobre que causa esto, pero se ha sospechado de una infeccion viral o de respuestas autoinmunitarias. Muy raramente, la Acalasia puede ser causada por un trastorno genetico hereditario o una infeccion.",
        "treatment": "El tratamiento de la Acalasia se centra en relajar o estirar la apertura del esfinter esofagico inferior, para que los alimentos y los liquidos puedan pasar mas facilmente a traves del tracto digestivo. El tratamiento especifico depende de tu edad, tu estado de salud y la gravedad de la acalasia. Los tratamientos no quirurgicos incluyen: dilatacion neumatica, botox (toxina botulinica tipo A), consumo de relajantes musculares como la nitroglicerina o la nifedipina. Los tratamientos quirurgicos incluyen: miotomia de heller, miotomia endoscopica por via oral."
    },
    {
        "id": 2,
        "name": "Balanitis",
        "symptoms": "Sarpullido rojo en la punta del pene. Dolor en el pene. Sensibilidad e hinchazon en la punta del pene. Comezon y molestia. Secrecion o pus debajo del prepucio que puede tener olor desagradable. Imposibilidad de retraer el prepucio.",
        "causes": "Existen varias causas de la balanitis incluidas las siguientes: Dermatitis de contacto. Medicamentos tales como ciertos tipos de analgesicos, somniferos, laxantes y antibioticos. Infecciones provocadas por bacterias y hongos tales como la Candida albicans. Lesiones en la punta del pene. Liquen escleroso. Balanitis de Zoon. Diabetes.",
        "treatment": "Ante esta enfermedad es importante lavarse el pene dos veces por dia y no usar jabones perfmados ni gel de ducha, solo agua. Los medicamentos para tratarla son antibioticos como la flucloxacilina o la eritromicina, crema antimicotica o creama esteroide suave. En muy raras ocasiones se usa la circuncision.",
    },
]