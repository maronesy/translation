# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 234 (printed ٢٣٣)."""

PAGE_NUMBER = 234
PRINTED_PAGE = "٢٣٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "زيدا ضربته») مثال لحرف التحضيض.",
     "en": "…Zayd—why do you not strike him?”—allā Zaydan ḍarabtahu), an example of the particle of urging."},
    {"type": "matn",
     "ar": "(وليس: «أزيد ذهب به» منه) أي: من باب الإضمار على شريطة التفسير،",
     "en": "(And “a-Zaydun dhuhiba bihi?” (Was Zayd taken away?) is not of it), that is, of the chapter of suppression on condition of explanation,"},
    {"type": "matn",
     "ar": "فإن «زيدا» فيه وإن كان يظن في بادئ النظر أنه مما أضمر عامله على شريطة التفسير، والمختار فيه النصب؛ لوقوع الاسم المذكور فيه بعد حرف الاستفهام،",
     "en": "for although “Zayd” in it is thought at first glance to be among those whose governor is suppressed on condition of explanation, with the accusative preferred in it because the noun mentioned occurs after a particle of interrogation,"},
    {"type": "matn",
     "ar": "لكن يظهر بعد تعمق النظر أنه ليس منه، فإنه وإن صدق عليه[[١]] أنه اسم بعده فعل مشتغل عنه بضميره،",
     "en": "it becomes clear after deeper consideration that it is not of it; for although it is true of it that it is a noun followed by a verb diverted from it by its pronoun,"},
    {"type": "matn",
     "ar": "لكنه ليس بحيث لو سلط عليه هو أو مناسبه لنصبه؛ لأن «ذهب به» لا يعمل النصب، وكذا مناسبه أعني: «أذهب».",
     "en": "it is not such that, were that [verb] or what corresponds to it brought to bear on it, it would put it in the accusative; because “dhuhiba bihi” does not govern the accusative, nor does what corresponds to it, namely “udhhiba” (was made to go)."},
    {"type": "matn",
     "ar": "فإن قلت: لا ينحصر المناسب في «أذهب» فليقدر مناسب آخر ينصبه مثل: «يلابس أو أذهب» على صيغة المعلوم،",
     "en": "If you say: what corresponds is not confined to “udhhiba,” so let another corresponding [verb] that puts it in the accusative be supposed, such as “yulābisu” or “adhhaba” in the active form;"},
    {"type": "matn",
     "ar": "فيكون تقديره: «زيدا يلابسه الذهاب به، أو يلابسه أحد بالذهاب به، أو أذهبه أحد».",
     "en": "its supposed form would then be: “Zayd—being taken away involves him,” or “someone involves him in being taken away,” or “someone took him away.”"},
    {"type": "matn",
     "ar": "قلنا: المراد بالمناسب ما يرادف الفعل المذكور أو يلازمه مع اتحاد ما أسند إليه[[٢]]، فالاتحاد فيما ذكرته مفقود.",
     "en": "We say: what is meant by “corresponding” is what is synonymous with the verb mentioned or entailed by it, with the identity of that to which it is predicated; and in what you mentioned that identity is lacking."},
    {"type": "matn",
     "ar": "وإذا كان الأمر كذلك (فالرفع) أي: رفع «زيد» في المثال (واجب) بالابتداء[[٣]]، ونصبه غير جائز بالمفعولية،",
     "en": "Since the matter is so, (the nominative), that is, the nominative of “Zayd” in the example, (is obligatory) by inchoation, and its accusative as an object is not allowed;"},
    {"type": "matn",
     "ar": "فليس من باب الإضمار على شريطة التفسير، فكيف مما يختار فيه النصب؟",
     "en": "so it is not of the chapter of suppression on condition of explanation—how then could it be among those in which the accusative is preferred?"},
    {"type": "matn",
     "ar": "(وكذا) أي: مثل: «أزيد ذهب به؟» قوله تعالى: (﴿وكل شيء فعلوه في الزبر﴾)[[٤]]، أي: في صحائف أعمالهم،",
     "en": "(And likewise), that is, like “a-Zaydun dhuhiba bihi?”, are His words, the Exalted: (“And everything they did is in the records”—wa-kullu shayʾin faʿalūhu fī al-zubur) (Qurʾān, Sūrat al-Qamar 54:52), that is, in the scrolls of their deeds."},
    {"type": "matn",
     "ar": "فهو ليس من باب الإضمار على شريطة التفسير؛ لأنه لو جعل منه لصار التقدير: «فعلوا كل شيء في الزبر»،",
     "en": "It is not of the chapter of suppression on condition of explanation; because were it made so, the supposed form would become “they did everything in the records,”"},
    {"type": "matn",
     "ar": "فقوله: «في الزبر» إن كان متعلقا بـ«فعلوا» فسد المعنى؛ لأن صحائف أعمالهم ليست محلا لفعلهم؛ لأنهم لم يوقعوا",
     "en": "and His words “fī al-zubur,” if attached to “faʿalū,” would spoil the meaning; because the scrolls of their deeds are not the locus of their doing, since they did not perform…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: ما حاصله: أن ليس الفعل الواقع بعده مشتغلا عنه بضميره؛ لأن معنى الاشتغال عنه بالضمير الاشتغال عن نصبه بنصب الضمير. والضمير هنا مرفوع المحل.",
     "en": "Shaykh al-Raḍī said, in substance: the verb occurring after it is not diverted from it by its pronoun, because being diverted from it by the pronoun means being diverted from putting it in the accusative by putting the pronoun in the accusative; and the pronoun here is nominative in position."},
    {"type": "pair",
     "ar": "وتجويز نصبه باعتبار إسناد ذهب إلى المصدر المدلول عليه به حتى يكون المعنى ذهب الذهاب به ضعيف لعدم اختصاص المصدر المدلول عليه بالفعل",
     "en": "Allowing its accusative by taking “dhuhiba” as predicated of the maṣdar it indicates, so that the meaning is “the taking-away of him was effected,” is weak, because the maṣdar indicated by the verb is not specified."},
    # REVIEW: print reads «مناب الفعل»; the sense (substitute for the agent) suggests «مناب الفاعل»; transcribed as printed.
    {"type": "pair",
     "ar": "يعني: ويجب أن يكون المصدر النائب مناب الفعل مخصوصا.",
     "en": "He means: the maṣdar standing in place of the verb [sic; probably “of the agent”] must be specified."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أنه لا يفهم اعتبار هذا القيد من تعريف ما أضمر عامله، فلا بد من الإشارة إليه في التعريف؛ إذ التعريفات محمولات على المتبادر.",
     "en": "Against this: taking this qualification into account is not understood from the definition of “what has its governor suppressed,” so it must be indicated in the definition, since definitions are taken in their most immediate sense."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كذا ذكره المصنف.",
     "en": "So the author stated it."},
    {"type": "pair",
     "ar": "وفيه أنه يجوز أن يكون مرفوعا بـ«أذهب» المقدر لرعاية الاستفهام. ويوافق ضابطة ذكرها في شرح المفصل.",
     "en": "Against this: it may be nominative by a supposed “udhhiba,” out of regard for the interrogation; and this accords with a rule he mentioned in the Sharḥ al-Mufaṣṣal."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة القمر:٥٢.",
     "en": "Sūrat al-Qamar 54:52."},
]
