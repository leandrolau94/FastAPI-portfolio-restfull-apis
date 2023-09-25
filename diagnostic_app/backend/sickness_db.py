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
    {
        "id": 3,
        "name": "Cancer",
        "symptoms": "Fatiga. Bulto o zona de engrosamiento que puede palparse debajo de la piel. Cambios de peso, como aumento o perdida de peso no intencionales. Cambios en la piel, como pigmentacion amarillenta, oscurecimiento o enrojecimiento de la piel, llagas q no se curan o cambios en los lunares existentes. Cambios en los habitos de evacuacion de la vejiga o los intestinos. Tos persistente o dificultad para respirar. Dificultad para tragar. Ronquera. Indigestion persistente o malestar despues de comer. Dolor muscular o articular persistente, sin causa aparente. Fiebre o sudoraciones nocturnas persistentes, sin causa aparente. Sangrado o hematomas sin causa aparente.",
        "causes": "El cancer es ocasionado por cambios (mutaciones) en el ADN dentro de las celulas. El ADN que hay en una celula esta dentro de un gran numero de genes, cada uno de los cuales contiene un grupo de instrucciones que le indica a la celula que funciones realizar, y como crecer y dividirse. Los errores en las instrucciones pueden provocar que la celula detenga su funcion normal y se convierta en una celula cancerosa.",
        "treatment": "Los tratamientos mas comunes son la cirugia, la quimioterapia y la radioterapia. Las opciones mas recientes incluyen la terapia dirigida, la inmunoterapia y la terapia hormonal laser entre otras. Otros tratamientos como la hipertermia, la terapia fotodinamica y la crioterapia tambien son usados.",
    },
    {
        "id": 4,
        "name": "Dengue",
        "symptoms": "Los sintomas leves del dengue pueden confundirse con otras enfermedades que causan fiebre, molestias y dolores o sarpullido. Fiebre. Dolor en los ojos. Dolor muscular. Dolor en los huesos. Dolor en las articulaciones. Dolor de cabeza. Nauseas o vomitos. Sarpullido. Estos sintomas duran por lo general entre 2 y 7 dias. ",
        "causes": "La fiebre del dengue es causada por cualquiera de los cuatro virus del dengue. No se puede contraer la fiebre del dengue por estar cerca de una persona infectada. En cambio, la fiebre del dengue se transmite a traves de las picaduras de mosquitos. Los dos tipos de mosquitos que mas a menudo propagan el virus del dengue son comunes dentro de las viviendas humanas y en sus alrededores. Cuando un mosquito pica a una persona infectada con un virus del dengue, el virus ingresa al mosquito. Luego, cuando el mosquito infectado pica a otra persona, el virus ingresa en el torrente sanguineo de la persona y causa una infeccion. Cuando te recuperes de la fiebre del dengue, tendras inmunidad a largo plazo al tipo de virus que te infecto, pero no a los otros tres tipos de virus de la fiebre del dengue. Esto significa que puedes volver a infectarte en el futuro por uno de los otros tres tipos de virus.",
        "treatment": "No existe un medicamento especifico para tratar el dengue. Si cree que tiene dengue descanse, tome acetaminofen para controlar la fiebre y aliviar el dolor, no tome aspirina ni ibuprofeno. Beba muchos liquidos como agua o bebidas con electrolitos agregados para permanecer hidratado.",
    },
    {
        "id": 5,
        "name": "ELA (Esclerosis Lateral Amiotrofica)",
        "symptoms": "Los sintomas de la ELA varian de una persona a otra. Los sintomas dependen de las celulas nerviosas afectadas. La ELA suele comenzar con debilidad muscular que se extiende y empeora con el tiempo. Los sintomas pueden incluir los siguientes: Dificultad para caminar o hacer las actividades diarias habituales. Tropezones y caidas. Debilidad en las piernas, los pies o los tobillos. Debilidad o torpeza en las manos. Dificultad para hablar o problemas para tragar. Debilidad asociada a calambres musculares y espasmos en brazos, hombros y lengua. Llanto, risa o bostezos intempestivos. Cambios en el pensamiento o comportamiento. Los musculos se debilitan a medida que mueren mas celulas nerviosas. Con el tiempo, esto afecta la masticacion, la deglucion, el habla y la respiracion.",
        "causes": "En alrededor del 10 por ciento de las personas con ELA se puede identificar una causa genetica. En el resto de los casos se desconoce la causa. Los investigadores continuan estudiando las posibles causas de la ELA. La mayoria de las teorias se centran en una interaccion compleja entre genes y factores ambientales, tales como: lagenetica, la edad el sexo, fumar, la exposicion a toxinas ambientales y el servicio militar por la exposicion a ciertos metales o sustancias quimicas, lesiones traumaticas, infecciones virales o el esfuerzo intenso q este conlleva.",
        "treatment": "No hay forma de revertir el curso de la esclerosis lateral amiotrofica. El tratamiento esta enfocado en reducir la progresion de los sintomas, previniendo complicaciones y promoviendo mayor tiempo de comodidad e independencia. El riluzol es el unico medicamento aprobado por la FDA para el tratamiento de la ELA. Este parece reducir la progresion de la enfermedad en algunas personas, probablemente reduciendo los niveles de glutamato. Algunos de los efectos secundarios que este medicamento puede causar son mareo, alteraciones gastrointestinales y alteracion en las pruebas de funcion hepatica. Ademas a consideracion de los medicos se puede hacer uso de terapias de cuidados respiratorios, terapias fisicas, terapias ocupacionales, terapias del lenguaje, terapias de apoyo nutricional y terapias de apoyo psicologico y social."
    },
    {
        "id": 6,
        "name": "Fibromialgia",
        "symptoms": "La fibromialgia es un trastorno caracterizado por dolor musculoesqueletico generalizado, acompañado por fatiga y problemas de sueño, memoria y estado de animo. Los sintomas que manifiesta esta enfermedad pueden ser: Dolor generalizado. Fatiga. Dificultades cognitivas.",
        "causes": "Debido a que suele ser hereditaria, podria haber ciertas mutaciones geneticas que hagan mas vulnerable a la persona de desarrollarla. Algunas infecciones parecen desencadenar o agravar la fibromialgia. Tambien puede desencadenarse por un suceso fisico, como un accidente automovilistico. Puede desencadenarse ademas como consecuencia del estres psicologico prolongado.",
        "treatment": "En general, los tratamientos para la fibromialgia consisten en medicamentos y estrategias de cuidado personal. No hay un solo tratamiento que funcione para todos los sintomas. Entre los medicamentos que pueden ayudar a reducir el dolor de la fibromialgia y a dormir mejor se encuentran los analgesicos de venta libre como el acetaminofen, el ibuprofeno y el naproxeno sodico. Los antidepresivos como la duloxetina y el milnacipran pueden ayudar tambien a aliviar el dolor y la fatiga asociados a la fibromialgia. El medico puede recetarte ademas la amitriptilina o el relajante muscular ciclobenzaprina para ayudar a promover el sueño. A menudo, los medicamentos anticonvulsivos diseñados para tratar la epilepsia ayudan a reducir ciertos tipos de dolor, por eso la gabapentina ayuda a reducir los sintomas de la fibromialgia. Tambien se promueve el uso de fisioterapia, terapia ocupacional y el asesoramiento psicologico.",
    },
]