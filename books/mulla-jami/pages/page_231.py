# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 231 (printed ٢٣٠)."""

PAGE_NUMBER = 231
PRINTED_PAGE = "٢٣٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "والجملة المعطوف عليها في كونهما فعليتين، نحو: «خرجت فزيدا لقيته».",
     "en": "…and the sentence coordinated to, in their both being verbal, as in “I went out, and Zayd—I met him” (kharajtu fa-Zaydan laqītuhu)."},
    {"type": "matn",
     "ar": "(وبعد حرف النفي) يعني: «ما، ولا، وإن، وليس، ولم، ولما، ولن» من هذه الجملة؛",
     "en": "(And after a particle of negation), meaning “mā,” “lā,” “in,” “laysa,” “lam,” “lammā” and “lan,” among this group;"},
    {"type": "matn",
     "ar": "إذ هي عاملة في المضارع، ولا يقدر معمولها، لضعفها في العمل[[١]] نحو: «ما زيدا ضربته»، ولا زيدا ضربته»، و«إن زيدا ضربته إلا تأديبا».",
     "en": "since these govern the imperfect, and their governed [verb] is not supposed, owing to their weakness in governing; as in “Zayd I did not strike” (mā Zaydan ḍarabtuhu), “nor Zayd did I strike,” and “Zayd I struck only to discipline him” (in Zaydan ḍarabtuhu illā taʾdīban)."},
    {"type": "matn",
     "ar": "(و) بعد (حرف الاستفهام) نحو: «أزيدا ضربته؟»، وإنما قال: «حرف الاستفهام»[[٢]]؛ لأنه يختار الرفع في اسم الاستفهام[[٣]]، مثل: «من أكرمته؟»",
     "en": "(And) after (a particle of interrogation), as in “Zayd—did you strike him?” (a-Zaydan ḍarabtahu?). He said “particle of interrogation” only because the nominative is preferred after an interrogative noun, as in “Who did you honour?” (man akramtahu?)."},
    {"type": "matn",
     "ar": "ولم يقل: «همزة الاستفهام» ليشمل مثل: «هل زيدا ضربته؟»، فإنه يجوز وإن استقبحه النحاة لاقتضاء «هل» لفظ الفعل؛",
     "en": "He did not say “the hamza of interrogation,” so as to include such as “hal Zaydan ḍarabtahu?” (Zayd—did you strike him?), for it is allowed, though the grammarians deem it ugly because “hal” requires the verb in its wording,"},
    {"type": "matn",
     "ar": "لأنه بمعنى «قد» في الأصل، فلا يكفي فيه تقدير الفعل[[٤]].",
     "en": "since it originally has the sense of “qad,” so supposing the verb does not suffice with it."},
    {"type": "matn",
     "ar": "(و) بعد («إذا» الشرطية) الدالة على المجازاة[[٥]] في الزمان نحو: «إذا عبد الله تلقاه فأكرمه».",
     "en": "(And) after (conditional “idhā”), which denotes requital (mujāzāt) in time, as in “When ʿAbd Allāh—you meet him, honour him” (idhā ʿAbda llāhi talqāhu fa-akrimhu)."},
    {"type": "matn",
     "ar": "(و) بعد («حيث»[[٦]]) الدلالة على المجازاة في المكان نحو: «حيث زيدا تجده فأكرمه».",
     "en": "(And) after (“ḥaythu”), denoting requital in place, as in “Wherever Zayd—you find him, honour him” (ḥaythu Zaydan tajiduhu fa-akrimhu)."},
    {"type": "matn",
     "ar": "(وفي) ما قبل (الأمر والنهي) يعني: موضع وقوع الاسم المذكور قبل الأمر والنهي",
     "en": "(And in) what precedes (a command and a prohibition), meaning: the place where the noun mentioned occurs before a command or a prohibition…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كأنه أراد أنه لا يقدر وجوبا؛ لأنه يكفي فيما هو بصدده نفي وجوب التقدير،",
     "en": "It seems he meant that it is not supposed obligatorily, because for his purpose the denial that supposing is obligatory suffices;"},
    {"type": "pair",
     "ar": "فلا يرد أن من وجوه الفرق بين لم ولما أنه يجوز حذف فعل «لما» دون «لم» كما سيأتي في محله، فلا يصح أنه لا يقدر معمول «لما» هذا،",
     "en": "so there is no objection that among the differences between “lam” and “lammā” is that the verb of “lammā” may be deleted but not that of “lam,” as will come in its place, so that it would not be correct that the governed [verb] of “lammā” is not supposed. This [is the answer];"},
    {"type": "pair",
     "ar": "لكن الظاهر أن جواز حذف الفعل بعد «لما» فيما سيأتي بمعنى يقابل الامتناع لا الوجوب.",
     "en": "but what is apparent is that the permissibility of deleting the verb after “lammā” in what will come is in a sense opposed to impossibility, not to obligation."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لو قال: «والاستفهام» عطفا على حرف النفي لخرج عنه نحو: «من ضربته؟»؛ لأنه ليس بعد الاستفهام، بل معه",
     "en": "Had he said “and interrogation,” coordinated to “particle of negation,” such as “man ḍarabtahu?” would be excluded from it, because [the noun] is not after the interrogation but together with it;"},
    {"type": "pair",
     "ar": "فما ذكره لا يصير نكتة لإدراج الحرف، وإنما يصير نكتة لذكر بعد، واختياره على معنى الاستفهام، فتأمل.",
     "en": "so what he mentioned is not a subtle point for including [the word] “particle”; it is only a subtle point for mentioning “after” and choosing it over the notion of interrogation. Reflect."},
    {"type": "pair",
     "ar": "وأما وجه ذكر الحرف فهو أن اسم الاستفهام يجب دخوله على الفعل الصريح، فلا يجوز «متى زيدا ضربته» صرح به الرضي.",
     "en": "As for the reason for mentioning “particle,” it is that an interrogative noun must enter on an explicit verb, so “matā Zaydan ḍarabtahu” (when did you strike Zayd?) is not allowed; al-Raḍī stated this explicitly."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إذا كان هو الاسم المحدود.",
     "en": "When it is itself the defined noun."},
    {"type": "pair",
     "ar": "أما إذا كان الاسم المحدود بعده نحو: «متى زيدا ضربته» كان حكمه حكم «هل» كما صرح به الشيخ الرضي.",
     "en": "But when the defined noun comes after it, as in “matā Zaydan ḍarabtahu,” its status is that of “hal,” as Shaykh al-Raḍī stated explicitly."},
    {"type": "pair",
     "ar": "فلو قال: أو بعد كلمة الاستفهام لكان أشمل، نعم لو قال: أو مع الاستفهام لم يصح لما ذكره قدس سره.",
     "en": "Had he said “or after an interrogative word,” it would have been more comprehensive. Yes, had he said “or with interrogation,” it would not be correct, for the reason he (may his secret be sanctified) mentioned."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مع جواز التلفظ به.",
     "en": "Since it may be pronounced."},
    {"type": "pair",
     "ar": "والسر في ذلك على ما ذكره أن «هل» طالبة للفعل، فإذا لم تجد فعلا تسلط عنه كما في «هل زيد خارج»،",
     "en": "The underlying reason, according to what he mentioned, is that “hal” seeks the verb: when it does not find a verb it is diverted from it (tasallaṭa ʿanhu), as in “hal Zaydun khārijun?” (Is Zayd going out?);"},
    {"type": "pair",
     "ar": "وإذا وجدت فعلا تذكرت الصحبة القديمة فلا ترضى إلا بأن تعانقه. ولهذا قبح «هل زيد خرج».",
     "en": "and when it finds a verb, it recalls the old companionship and is content with nothing but embracing it. For this reason “hal Zaydun kharaja?” is ugly."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لكنها قاصرة عن إفادتها؛ إذ ليس مدخولها على خطر الوجود، بل قطعي الحصول.",
     "en": "But it falls short of conveying it, since what it enters on is not uncertain of existence but certain to occur."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "دون «حيثما»، فإن حكمها حكم «متى».",
     "en": "Not “ḥaythumā,” for its status is that of “matā.”"},
]
