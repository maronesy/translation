# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 249 (printed ٢٤٨)."""

PAGE_NUMBER = 249
PRINTED_PAGE = "٢٤٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأن العطف على الضمير المجرور بلا إعادة» from the foot of PDF p. 248.
    {"type": "matn",
     "ar": "الجار غير جائز، ولم يجز عطف «عمرا» على الشأن[[١]]؛ إذ السؤال عن شأنهما لا عن شأن أحدهما ونفس الآخر.",
     "en": "…the preposition is not permissible; and conjoining “ʿAmr” to “business” (al-shaʾn) is not permissible, since the question is about the business of both, not about the business of one of them and the person of the other."},
    {"type": "matn",
     "ar": "وإنما حكمنا[[٢]] بمعنوية الفعل في هذه الأمثلة (لأن المعنى: «ما تصنع؟») وما يماثله،",
     "en": "We judged the verb in these examples to be notional only (because the meaning is “What are you doing?”) and the like;"},
    {"type": "matn",
     "ar": "فمعنى «ما شأنك وزيدا؟» ما تصنع وزيدا، ومعنى «ما لك وزيدا؟»: ما تصنع وزيدا، ومعنى «ما لزيد وعمرو؟» ما يصنع زيد وعمرو.",
     "en": "so the meaning of “What is your business with Zayd?” is “What are you doing with Zayd?”; the meaning of “What is with you and Zayd?” is “What are you doing with Zayd?”; and the meaning of “What is with Zayd and ʿAmr?” is “What are Zayd and ʿAmr doing?”"},

    {"type": "section", "ar": "[الحال]",
     "en": "The Circumstantial Accusative (al-Ḥāl)"},

    {"type": "matn",
     "ar": "(الحال[[٣]]) لما فرغ من المفاعيل شرع في الملحقات بها",
     "en": "(The circumstantial accusative (al-ḥāl)): having finished with the objects, he begins on what is attached to them."},
    {"type": "matn",
     "ar": "(وهو ما يبين هيئة الفاعل[[٤]] أو المفعول به) أي: من حيث هو فاعل أو مفعول به[[٥]]، كما هو الظاهر،",
     "en": "(It is what makes clear the state (hayʾa) of the agent or of the direct object), that is, insofar as it is agent or direct object, as is apparent,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه بحث لجواز العطف بجعل الكلام على حذف المضاف، وإقامة المضاف إليه مقامه،",
     "en": "This is open to discussion, since conjunction is permissible by taking the expression to involve the elision of the first term of the genitive construction (al-muḍāf), with the second term (al-muḍāf ilayhi) put in its place;"},
    # REVIEW: «أعمال» printed (with hamza above the alif); sense requires «إعمال» (“making to govern”); transcribed as printed.
    {"type": "pair",
     "ar": "والنصب وإن ترجح بالسلامة عن الحذف يرجح الرفع بالاستغناء عن أعمال العامل المعنوي.",
     "en": "and the accusative, though preferred for being free of elision, the nominative is preferred for dispensing with making a notional governor govern."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "تكلف في بيان المعلل بقوله: لأن المعنى ما تصنع؟",
     "en": "He strained in stating what is being explained by his words “because the meaning is ‘What are you doing?’”"},
    {"type": "pair",
     "ar": "والأظهر أن المعلل النصب أي: نصب الاسم في هذين المثالين؛ لأن المعنى ما تصنع؟",
     "en": "It is more evident that what is being explained is the accusative, that is, the accusative of the noun in these two examples, because the meaning is “What are you doing?”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لفظ يغلب فيه التأنيث من حال بمعنى تغير،",
     "en": "A word in which the feminine predominates, from ḥāla in the sense of “to change”;"},
    {"type": "pair",
     "ar": "ففيه تنبيه على أن الحال لا يكون أمرا خلقيا، فلا يجوز جاءني زيد أحمر أو طويلا.",
     "en": "so it contains a hint that the ḥāl is not an innate attribute; hence “Zayd came to me red” or “tall” is not permissible."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الهيئة في الأصل: الحالة الظاهرة للمتهيئ للشيء، كذا في المغرب.",
     "en": "Al-hayʾa originally means the outward state of one disposed for a thing; so in al-Mughrib."},
    {"type": "pair",
     "ar": "والمراد هنا الحالة، وهي أعم من أن يكون بحسب تحققها، وهي الحال المحققة أو بحسب تقديرها وهي الحال المقدرة،",
     "en": "What is meant here is the state, which is more general than being according to its realization, namely the realized ḥāl (al-ḥāl al-muḥaqqaqa), or according to its supposition, namely the anticipated ḥāl (al-ḥāl al-muqaddara),"},
    {"type": "pair",
     "ar": "نحو قوله تعالى: ﴿فادخلوها خالدين﴾ (سورة الزمر: ٧٣)، أي: مقدرين الخلود.",
     "en": "as in His words, the Exalted: “So enter it, abiding eternally” (Qurʾān, Sūrat al-Zumar 39:73), that is, destined to abide eternally;"},
    {"type": "pair",
     "ar": "نحو خط هذا الثوب قميصا، ونحو قوله تعالى: ﴿وبشرناه بإسحاق نبيا﴾ (سورة الصافات: ١١٢)، أي: مقدرة نبوته.",
     "en": "as in “Sew this cloth [into] a shirt,” and as in His words, the Exalted: “And We gave him tidings of Isaac, a prophet” (Qurʾān, Sūrat al-Ṣāffāt 37:112), that is, his prophethood being destined."},
    {"type": "pair",
     "ar": "وأيضا هي أعم من أن يكون باعتبار حال نفس الفاعل والمفعول، أو باعتبار حال متعلقهما،",
     "en": "Again, it is more general than being with regard to the state of the agent and object themselves, or with regard to the state of what is connected to them;"},
    {"type": "pair",
     "ar": "فلا يرد النقض بـ«جاء زيد وأبوه قائم»، لكن يرد النقض بقولك: «أتيتك وزيد قائم».",
     "en": "so no objection arises from “Zayd came, his father standing”; but an objection does arise from your saying “I came to you while Zayd was standing.”"},
    {"type": "pair",
     "ar": "وينسب إلى صاحب المفصل في دفعه أنه قال في بعض حواشيه: إن \"وزيد قائم\" يبين هيئة لازم الفاعل أو المفعول به، أعني: زمان الإتيان.",
     "en": "It is attributed to the author of al-Mufaṣṣal, in answering it, that he said in one of his glosses: “while Zayd was standing” makes clear the state of what is concomitant with the agent or the direct object, namely the time of the coming."},
    {"type": "pair",
     "ar": "وقد استمر في كلامهم التعبير عن الملزوم باللازم، فكان هيئة اللازم هيئة الملزوم.",
     "en": "It has been constant in their usage to express the entailing by the entailed; so the state of the entailed is the state of the entailing."},
    {"type": "pair",
     "ar": "وذلك بعيد، لأن قيام زيد ليس هيئة لزمان زيد إلا بتأويل،",
     "en": "This is far-fetched, because Zayd’s standing is not a state of Zayd’s time except by interpretation;"},
    {"type": "pair",
     "ar": "وإن زمان الإتيان لما كان مباينا مفارقا عن فاعل الإتيان، وعن مفعوله لم يلائم دعوى الاتحاد بينهما على أن عبارة التعريف لا تدل عليه دلالة ظاهرة.",
     "en": "and since the time of the coming is distinct and separable from the agent of the coming and from its object, the claim of unity between them does not fit; besides, the wording of the definition does not plainly indicate it."},
    {"type": "pair",
     "ar": "وقال الشيخ الرضي: الحق أن الحال على ضربين: منتقلة ومؤكدة. ولكل منهما حد لاختلاف ماهيتهما،",
     "en": "Shaykh al-Raḍī said: the truth is that the ḥāl is of two kinds, transient (muntaqila) and corroborative (muʾakkida); each has its own definition, because their quiddities differ."},
    {"type": "pair",
     "ar": "فحد المنتقلة جزء كلام يتقيد بوقت حصول مضمونه تعلق الحدث الذي في ذلك الكلام بالفاعل أو المفعول أو بما يجري مجراهما،",
     "en": "The definition of the transient one: a part of speech by the time of whose content’s occurrence is restricted the connection of the event in that speech with the agent or object, or with what takes their place."},
    {"type": "pair",
     "ar": "وبقولنا: جزء كلام يخرج الجملة الثانية في ركب زيد ويركب مع ركوب غلامه إذا لم نجعلهما حالا،",
     "en": "By our words “a part of speech” is excluded the second sentence in “Zayd rode, and he rides along with his servant’s riding,” when we do not make them a ḥāl."},
    {"type": "pair",
     "ar": "وحد المؤكدة اسم غير حدث يجيء مقررا لمضمون جملة. وقولنا: «غير حدث» احتراز عن نحو: «رجع رجوعا».",
     "en": "The definition of the corroborative one: a noun, not an event, that comes to confirm the content of a sentence. Our words “not an event” guard against such a case as “He returned a returning.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "في دلالة الحال على أن مدلولها هيئة للفاعل، أو المفعول به من حيث إنه فاعل أو مفعول نحوي، تأمل.",
     "en": "On the ḥāl indicating that what it denotes is a state of the agent or the direct object insofar as it is a grammatical agent or object, there is room for reflection."},
    {"type": "pair",
     "ar": "نعم إنها تدل على هيئة الفاعل أو المفعول في زمان تعلق الفعل بهما.",
     "en": "Yes, it does indicate the state of the agent or object at the time of the action’s connection with them."},
]
