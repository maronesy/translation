# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 339 (printed ٣٣٨)."""

PAGE_NUMBER = 339
PRINTED_PAGE = "٣٣٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فحسن الاختصار بترك التأكيد،» at the foot of PDF p. 338.
    {"type": "matn",
     "ar": "سواء كان الفصل قبل حرف العطف (نحو: «ضربت اليوم وزيد») أو بعده كقوله تعالى: ﴿ما أشركنا ولا آباؤنا﴾[[١]]",
     "en": "…whether the separation comes before the conjunctive particle, (as in “ḍarabtu al-yawma wa-Zaydun” [I struck today, and Zayd]), or after it, as in His words, Exalted is He, “We would not have associated [others with Allah], nor would our fathers” (Qurʾān, Sūrat al-Anʿām 6:148);"},
    {"type": "matn",
     "ar": "فإن المعطوف هو «آباؤنا»، و«لا» زائدة بعد حرف العطف لتأكيد النفي،",
     "en": "for the conjoined noun is “ābāʾunā” (our fathers), and “lā” is redundant after the conjunctive particle, to reinforce the negation."},
    # REVIEW: «متسايان» printed, apparently for «متساويان»; transcribed as printed.
    {"type": "matn",
     "ar": "وإنما قال: «يجوز تركه»، فإنه قد يؤكد بالمنفصل مع الفصل، كقوله تعالى: ﴿فكبكبوا فيها هم والغاوون﴾[[٢]] وقد لا يؤكد، والأمران متسايان.",
     "en": "He said “its omission is permitted” only because it is sometimes corroborated by a detached [pronoun] despite the separation, as in His words, Exalted is He, “Then they will be toppled into it, they and the deviators” (Qurʾān, Sūrat al-Shuʿarāʾ 26:94), and sometimes it is not corroborated; and the two are equal."},
    {"type": "matn",
     "ar": "هذا، واعلم أن مذهب البصريين[[٣]] أن التأكيد بالمنفصل هو الأولى، ويجوزون العطف بلا تأكيد ولا فصل، لكن على قبح، والكوفيون يجوزونه بلا قبح.",
     "en": "So much for this. Know that the doctrine of the Baṣrans is that corroboration by a detached [pronoun] is preferable, and they permit conjunction without corroboration or separation, but as an ugly usage; while the Kūfans permit it without ugliness."},
    {"type": "matn",
     "ar": "(وإذا عطف على الضمير المجرور أعيد الخافض) حرفا كان أو اسما[[٤]]؛",
     "en": "(When [a noun] is conjoined to the genitive pronoun, the governor of the genitive [al-khāfiḍ] is repeated), whether it is a particle or a noun,"},
    {"type": "matn",
     "ar": "لأن اتصال الضمير المجرور بجاره أشد من اتصال الفاعل المتصل بفعله؛ لأن الفاعل إن لم يكن ضميرا متصلا جاز انفصاله، والمجرور لا ينفصل من جاره،",
     "en": "because the attachment of the genitive pronoun to its governor is closer than the attachment of the attached agent to its verb: for the agent, if it is not an attached pronoun, may be detached, whereas the genitive noun is never detached from its governor."},
    {"type": "matn",
     "ar": "فكره العطف عليه، إذ يكون كالعطف على بعض حروف الكلمة،",
     "en": "So conjunction to it is disliked, since it would be like conjoining to some of the letters of the word;"},
    {"type": "matn",
     "ar": "وليس للمجرور ضمير منفصل -كما يجيء في المضمرات- حتى يؤكد به أولا ثم يعطف عليه كما عمل في المرفوع المتصل،",
     "en": "and the genitive has no detached pronoun—as will come in [the chapter on] pronouns (al-muḍmarāt)—by which it could first be corroborated and then conjoined to, as was done with the attached nominative;"},
    {"type": "matn",
     "ar": "وفي استعارة المرفوع له مذلة ولا يكتفى بالفصل؛",
     "en": "to borrow the nominative [pronoun] for it would be a humiliation; nor is separation sufficient,"},
    {"type": "matn",
     "ar": "لأن الفصل لا تأثير له إلا في جواز ترك التأكيد بالمنفصل للاختصار، فحيث لا يمكن التأكيد بالمنفصل لعدمه لا يتصور له أثر، فكيف يكتفى به؟",
     "en": "because separation has no effect except in permitting the omission of corroboration by a detached [pronoun] for brevity; so where corroboration by a detached [pronoun] is impossible because there is none, no effect of it can be conceived; how then could it suffice?"},
    {"type": "matn",
     "ar": "فلم يبق إلا إعادة العامل الأول (نحو: «مررت بك وبزيد») و«المال بيني وبين زيد»،",
     "en": "So nothing remains but to repeat the first governor, (as in “marartu bika wa-bi-Zaydin” [I passed by you and by Zayd]) and “al-mālu baynī wa-bayna Zaydin” (the property is between me and Zayd)."},
    {"type": "matn",
     "ar": "والمعطوف هو المجرور، والعامل مكرر، وجره بالأول، والثاني كالعدم معنى؛ بدليل قولهم: «بيني وبينك»؛ إذ «بين» لا يضاف إلا إلى المتعدد[[٥]].",
     "en": "The conjoined noun is the genitive noun; the governor is repeated, its genitive is by the first, and the second is as if absent in meaning; as shown by their saying “baynī wa-baynaka” (between me and you), since “bayna” is annexed only to what is more than one."},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 338 (footnote ٥ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "ضربت أنا وزيد اليوم يطول الكلام كطوله إذا قيل: ضربت أنا اليوم وزيد،",
     "en": "…“ḍarabtu anā wa-Zaydun al-yawma” (I struck, I and Zayd, today), the utterance grows long just as when one says “ḍarabtu anā al-yawma wa-Zaydun”."},
    {"type": "pair",
     "ar": "فالوجه أن يقال: جوز العطف على ما هو كالجزء من الفعل احترازا عن طول الفصل بين المعطوف والمعطوف عليه.",
     "en": "So the right way is to say: conjunction to what is like a part of the verb was permitted to avoid a long separation between the conjoined noun and the noun conjoined to."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الأنعام: ١٤٨.",
     "en": "Sūrat al-Anʿām 6:148."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الشعراء: ٩٤.",
     "en": "Sūrat al-Shuʿarāʾ 26:94."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إشارة إلى أنه خالف القبيلتين؛ لأنه أوجب التأكيد حيث قال: أكد.",
     "en": "An indication that he [the author] departed from both parties, since he made corroboration obligatory when he said “it is corroborated”."},
    {"type": "pair",
     "ar": "إن قلت: يجوز أن يريد به الوجوب الاستحساني؟ قلت: يأبى ذلك ما ذكره في بحث المفعول معه من أنه إذا لم يجز العطف تعين النصب مثل: جئت وزيدا.",
     "en": "If you say: may he not mean by it an obligation of approbation (wujūb istiḥsānī)? I say: what he stated in the discussion of the mafʿūl maʿahu (the object of accompaniment) rejects that, namely that when conjunction is not permitted the accusative is required, as in “jiʾtu wa-Zaydan” (I came along with Zayd)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا يعاد العامل الاسمى إلا إذا لم يشك أنه لا معنى له، وأنه جلب لهذا الغرض كبين، فإنه لا يتصور إلا بين اثنين،",
     "en": "Shaykh al-Raḍī said: the nominal governor is repeated only when there is no doubt that it has no meaning [of its own] and was brought in for this purpose, like “bayna”, which is conceivable only between two;"},
    {"type": "pair",
     "ar": "فإن التبس نحو: غلامك وغلام زيد، وأنت تريد غلاما واحدا لم يجز إلا إذا قام قرينة دالة على المقصود.",
     "en": "if there is ambiguity, as in “ghulāmuka wa-ghulāmu Zaydin” (your slave and Zayd’s slave) when you mean a single slave, it is not permitted unless there is a contextual indication (qarīna) pointing to what is intended."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فلا يتصور عطف المضاف. وفي نحو: مررت بك وبزيد إن أمكن أن يكون للباء الثاني معنى؛ إذ يمكن استئناف معنى الجار والمجرور.",
     "en": "So conjunction of the annexed noun is inconceivable. In such as “marartu bika wa-bi-Zaydin”, it is possible for the second bāʾ to have a meaning, since the meaning of the preposition and its genitive can be taken up afresh;"},
    {"type": "pair",
     "ar": "ويكون بسبب الاستئناف له معنى، لكن لما كان اجتلابه كاجتلاب بين كان الظاهر أن يكون حكمه حكم بين.",
     "en": "and by reason of this fresh start it would have a meaning; but since bringing it in is like bringing in “bayna”, the evident [view] is that its ruling is the ruling of “bayna”."},
]
