# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 226 (printed ٢٢٥)."""

PAGE_NUMBER = 226
PRINTED_PAGE = "٢٢٥"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[اشتغال]",
     "en": "Preoccupation of the Governor (Ishtighāl)"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وهو) أي: ما أضمر عامله على شريطة التفسير (كل اسم[[١]] بعده فعل[[٢]] أو شبهه).",
     "en": "(It), that is, [the noun] whose governor is suppressed on condition of explanation (ʿalā sharīṭat al-tafsīr), (is every noun after which comes a verb or what resembles a verb)."},
    {"type": "matn",
     "ar": "احترز به[[٣]] عن نحو: «زيد أبوك»،",
     "en": "By this he excluded the like of “Zaydun abūka” (Zayd is your father)."},
    {"type": "matn",
     "ar": "ولا يريد به أن يليه الفعل أو شبهه متصلا به، بل أن يكون الفعل أو شبهه جزء الكلام الذي بعده[[٤]]",
     "en": "He does not mean that the verb or what resembles it follows it directly, but that the verb or what resembles it is part of the utterance that comes after it,"},
    {"type": "matn",
     "ar": "نحو: «زيدا عمرو ضربه، وزيدا أنت ضاربه»[[٥]]",
     "en": "as in “Zaydan ʿAmrun ḍarabahu” (Zayd, ʿAmr struck him) and “Zaydan anta ḍāribuhu” (Zayd, you are striking him)."},
    {"type": "matn",
     "ar": "(مشتغل[[٦]]) ذلك الفعل أو شبهه (عنه[[٧]]) أي: عن العمل في ذلك الاسم (بضميره) أي: بالعمل في ضميره",
     "en": "(That verb or what resembles it being preoccupied away from it), that is, from governing that noun, (by its pronoun), that is, by governing its pronoun,"},
    {"type": "matn",
     "ar": "(أو في متعلقه) أي: متعلق ذلك الاسم أو متعلق ضميره[[٨]].",
     "en": "(or [by governing] what is connected with it), that is, what is connected with that noun or with its pronoun."},
    {"type": "matn",
     "ar": "وحاصله: أن يكون الفعل أو شبهه مشتغلا بالعمل في ضمير ذلك الاسم أو متعلقه فارغا عن العمل فيه بسبب ذلك الاشتغال لا بسبب آخر",
     "en": "In sum: the verb or what resembles it is preoccupied with governing the pronoun of that noun or what is connected with it, and is free of governing the noun itself because of that preoccupation, not for some other reason,"},
    {"type": "matn",
     "ar": "بحيث (لو سلط[[٩]]) لمجرد",
     "en": "such that (if it were given power), merely…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أقحم لفظ «كل» لبيان المانعية.",
     "en": "He inserted the word “kull” (every) to show that the definition excludes [what does not belong]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يقل: كل مفعول؛ لأن المتبادر من المفعول المفعول به.",
     "en": "He did not say “every object” (mafʿūl), because what is first understood by mafʿūl is the direct object (al-mafʿūl bihi),"},
    {"type": "pair",
     "ar": "وما أضمر عامله أعم من المفعول به، حتى يتناول المفعول فيه، وإن كان البحث فيما أضمر عامله الذي هو المفعول به،",
     "en": "whereas [the noun] whose governor is suppressed is more general than the direct object, so as to include the adverbial object (al-mafʿūl fīhi), even though the discussion concerns that whose suppressed governor [governs] the direct object;"},
    {"type": "pair",
     "ar": "ولأن التصريح بالمفعول يخرج ما عدا صور النصب.",
     "en": "and because stating “object” explicitly would exclude the cases other than the accusative."},
    {"type": "pair",
     "ar": "ولم تكن من مظان الإضمار على شريطة التفسير بخلاف الاسم، فإنه يدخله بحسب الظاهر،",
     "en": "They would then not be among the places where suppression on condition of explanation is expected; unlike “noun,” which includes them on the face of it,"},
    {"type": "pair",
     "ar": "فيكون ما عدا صور النصب من مظان الإضمار على شريطة التفسير، ويناسب أن يبين أحواله.",
     "en": "so that the cases other than the accusative are among the places where suppression on condition of explanation is expected, and it is fitting that their conditions be explained."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بقوله: بعده فعل أو شبهه.",
     "en": "That is, by his words “after which comes a verb or what resembles it.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: بحيث يصح أن يكون ذلك الاسم من تتمة هذا الكلام؛",
     "en": "That is, such that that noun may properly be part of the completion of this utterance,"},
    {"type": "pair",
     "ar": "إذ سلط ذلك الفعل أو شبهه عليه بقرينة قوله: لو سلط عليه هو أو مناسبه لنصبه.",
     "en": "if that verb or what resembles it were given power over it, as indicated by his words “if it or what corresponds to it were given power over it, it would put it in the accusative.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا بد لشبه الفعل مما يعتمد عليه إما قبل الاسم المحدود نحو: زيد هندا ضاربها وأزيدا ضاربه العمران،",
     "en": "What resembles the verb must have something it leans on (iʿtimād), either before the noun being defined, as in “Zaydun Hindan ḍāribuhā” and “a-Zaydan ḍāribuhu al-ʿAmrān?”,"},
    {"type": "pair",
     "ar": "أو بعده كالمثال المذكور في الشرح ومثل: «زيدا ضاربه عمرو» على أن يكون «عمرو» مبتدأ و«ضاربه» خبرا له.",
     "en": "or after it, as in the example given in the commentary, and as in “Zaydan ḍāribuhu ʿAmrun,” taking “ʿAmr” as the mubtadaʾ and “ḍāribuhu” as its khabar."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "صفة لأحد الأمرين المفهوم من لفظة «أو»، أو لكل من الأمرين على سبيل التنازع.",
     "en": "[Mushtaghil is] a qualifier of “one of the two,” understood from the word “aw” (or), or of each of the two by way of contention (tanāzuʿ)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "متعلق بالاشتغال لتضمين معنى الفراغ، أو لأن الاشتغال بمعنى الإعراض.",
     "en": "[“ʿAnhu” is] attached to “ishtighāl,” because it is made to include the sense of being free, or because ishtighāl here means turning away."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "في هذا التوجيه تصريح بالتزام الضمير، وتعلقه بالضمير بأن يكون الضمير من تتمته بوجه ما، ويتصور ذلك بوجوه:",
     "en": "This explanation states explicitly that the pronoun is required, and that [the connected word] is connected with the pronoun in that the pronoun forms part of its completion in some way. This can be conceived in several ways."},
    {"type": "pair",
     "ar": "منها: أن يكون المتعلق مضافا إلى الضمير سواء كان ذلك المتعلق معمولا بالأصالة للفعل وشبهه نحو: «زيدا ضربت غلامه» أو بالتبعية نحو: «زيدا ضربت عمرا وغلامه».",
     "en": "Among them: that the connected word is annexed to the pronoun, whether that connected word is governed by the verb or what resembles it directly, as in “Zaydan ḍarabtu ghulāmahu” (Zayd, I struck his servant), or as a follower, as in “Zaydan ḍarabtu ʿAmran wa-ghulāmahu” (Zayd, I struck ʿAmr and his servant)."},
    {"type": "pair",
     "ar": "ومنها: أن يكون المتعلق موصولا أو موصوفا بعامل الضمير أو معطوفا عليه موصول عامل الضمير أو موصوفه نحو: «زيدا لقيت عمرا، و«الذي يضربه أو رجلا يضربه».",
     "en": "Among them: that the connected word is a relative or qualified noun [linked] by the governor of the pronoun, or is coordinated with the relative or qualified noun of the pronoun’s governor, as in “Zaydan laqītu ʿAmran wa-lladhī yaḍribuhu, aw rajulan yaḍribuhu” (Zayd, I met ʿAmr and the one who strikes him, or a man who strikes him)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "إشارة إلى قوله: لو سلط صفة بعد صفة لأحد الأمرين.",
     "en": "This points to his words “if it were given power” being a qualifier after a qualifier of “one of the two.”"},
]
