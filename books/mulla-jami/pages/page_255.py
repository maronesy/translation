# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 255 (printed ٢٥٤)."""

PAGE_NUMBER = 255
PRINTED_PAGE = "٢٥٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Comments on the verse «(وأرسلها العراك) ولم يذدها ...» quoted at the foot of PDF p. 254.
    {"type": "matn",
     "ar": "البيت للبيد يصف الحمار الوحش، والأتن يقول: «أرسل الحمار الوحش الأتن»،",
     "en": "The verse is by Labīd, describing the wild ass and the she-asses; he says: “The wild ass sent the she-asses [to the water].”"},
    {"type": "matn",
     "ar": "وكان المراد بالإرسال: البعث أو التخلية[[١]] بين المرسل وما يريد،",
     "en": "What is meant by “sending” is dispatching, or leaving free (takhliya) what is sent to what it wants;"},
    {"type": "matn",
     "ar": "أي: أرسلها معتركة أي: متزاحمة، «ولم يذدها» أي: لم يمنعها عن العراك،",
     "en": "that is, he sent them jostling, that is, crowding one another; “and did not drive them back,” that is, he did not prevent them from crowding;"},
    {"type": "matn",
     "ar": "«ولم يشفق» أي: لم يخف على نغص الدخال أي: على أنه لم يتم شرب بعضها للماء بالدخال،",
     "en": "“nor feared,” that is, he was not afraid of the spoiling of al-dikhāl, that is, that some of them would not complete their drinking of the water because of the crowding in."},
    {"type": "matn",
     "ar": "و«الدخال» هو أن يشرب البعير ثم يرد[[٢]] من العطن إلى الحوض[[٣]]، ويدخل بين بعيرين عطشانين، ليشرب منه ما عساه لم يكن شرب منه،",
     "en": "“Al-dikhāl” is when a camel drinks, then is brought back from the resting place (ʿaṭan) to the trough and enters between two thirsty camels, to drink of it what perhaps it had not drunk;"},
    {"type": "matn",
     "ar": "ولعل المراد به ههنا نفس مداخلة بعضها في بعض أو المعنى على نغص مثل نغص الدخال.",
     "en": "perhaps what is meant by it here is simply their pressing in among one another; or the sense is “a spoiling like the spoiling of dikhāl.”"},
    {"type": "matn",
     "ar": "(و«مررت به وحده»[[٤]] ونحوه) مثل: «فعلته جهدك»[[٥]] بلفظ الخطاب",
     "en": "(And “I passed by him alone” and the like), such as “I did it with your utmost effort,” in the second-person form,"},
    {"type": "matn",
     "ar": "(متأول[[٦]]) بالنكرة فلا يرد نقضا على قاعدة اشتراط كونها نكرة، وتأويلها على وجهين:",
     "en": "(is to be reinterpreted) as indefinite, so it does not stand as an objection to the rule stipulating that it be indefinite. Its reinterpretation is in two ways:"},
    {"type": "matn",
     "ar": "أحدهما: أنها مصادر لأفعال محذوفة[[٧]] أي: «تعترك[[٨]] العراك» و«ينفرد وحده»",
     "en": "the first: that they are maṣdars of elided verbs, that is, “they jostle a jostling” and “he is alone by himself”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: print reads «لم يذددها» (the verse has «يذدها»); transcribed as printed.
    {"type": "pair",
     "ar": "الظاهر هو الثاني. وعطف لم يذددها للتفسير.",
     "en": "The second is what appears; and “and did not drive them back” is conjoined by way of explanation."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: print reads «مضاف مجهول» (sense suggests «مضارع مجهول», passive imperfect); transcribed as printed, translated by sense.
    {"type": "pair",
     "ar": "مضاف مجهول.",
     "en": "[Yuraddu]: a passive imperfect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كتب في الحاشية: العطن: ما حول الحوض والبئر من مبارك الإبل. والمبرك المناخ.",
     "en": "He wrote in the gloss: al-ʿaṭan is the camels’ kneeling places around the trough and the well; and the mabrak is the place where camels are made to kneel (munākh)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال قدس سره في الحاشية: الوحد مصدر «وحد يحد يقال: وحدا ووحدة كوعد يعد وعدا ووعدة، انتهى.",
     "en": "He—may his secret be sanctified—said in the gloss: al-waḥd is the maṣdar of “waḥada yaḥidu”; one says waḥdan and ḥidatan, like waʿada yaʿidu waʿdan and ʿidatan. End of quotation."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: وحده لازم الإفراد والتذكير والإضافة إلى الضمير، ولازم النصب إلا في مواضع مخصوصة.",
     "en": "Shaykh al-Raḍī said: “waḥdahu” is always singular, masculine and annexed to a pronoun, and always accusative except in particular places."},
    {"type": "pair",
     "ar": "قيل: يجوز أن يقال: إن أصله التاء، ثم حذفت لقيام المضاف إليه مقامه كما قيل في «أقام الصلاة».",
     "en": "It has been said: it may be said that its base had the tāʾ, which was then dropped because the muḍāf ilayhi stands in its place, as was said of “aqāma al-ṣalāt.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بصيغة الخطاب قال قدس سره في الحاشية: الجهد ههنا بضم الجيم، والجهد بفتح الجيم وضمها الاجتهاد.",
     "en": "In the second-person form. He—may his secret be sanctified—said in the gloss: al-juhd here is with ḍamma on the jīm; and jahd, with fatḥa or ḍamma on the jīm, is exertion."},
    {"type": "pair",
     "ar": "وقال الفراء: هو بفتح الجيم المشقة، وبضمها الطاقة.",
     "en": "Al-Farrāʾ said: with fatḥa on the jīm it is hardship, and with ḍamma it is capacity."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: كل واحد منها كذا قيل. قلت: وكذا ضمير نحوه، بل هو أحق بالتأويل.",
     "en": "That is, each one of them—so it has been said. I say: likewise the pronoun in “naḥwuhu” (the like of it); indeed it is more deserving of reinterpretation."},
    {"type": "pair",
     "ar": "والأظهر أن المراد بنحو: العراك المعرف باللام من المصادر وغيرها نحو: مررت بهم الجم الغفير أي: كثيرا ساترا بكثرتهم وجه الأرض،",
     "en": "What is most apparent is that by “the like of” al-ʿirāk is meant what is made definite by the lām, among maṣdars and others, as in “I passed by them, al-jamma al-ghafīr,” that is, numerous, covering the face of the earth by their multitude;"},
    {"type": "pair",
     "ar": "ونحوه: دخلوا الأول فالأول، أي: أولا فأولا،",
     "en": "and its like: “They entered the first then the first,” that is, “one after another”;"},
    {"type": "pair",
     "ar": "وبنحو: وحده المضاف من المصادر ومن غيرها نحو: جاءني الرجال ثلاثتهم إلى عشرتهم،",
     "en": "and by “the like of” waḥdahu is meant what is annexed, among maṣdars and others, as in “The men came to me, the three of them,” up to “the ten of them”;"},
    {"type": "pair",
     "ar": "فإن هذه الأسماء الثمانية مضافات إلى ضمائر ما تقدم منصوبات على الحالية في الحجاز لوقوعها موقع النكرة، فإنها في معنى مجتمعين في المجيء،",
     "en": "for these eight nouns, annexed to pronouns referring to what precedes, are in the accusative as ḥāls in the Ḥijāz because they stand in the position of the indefinite, since they mean “gathered together in coming,”"},
    {"type": "pair",
     "ar": "وتأكيدات لما قبلها في تميم معربات بإعرابه.",
     "en": "while in Tamīm they are corroboratives (taʾkīd) of what precedes them, inflected with its inflection."},
    {"type": "pair",
     "ar": "ولا يبعد أن يجعل الحال التي هي جملة داخلة في نحوه؛ لأن الجملة ليست بنكرة؛ إذ هي كالمعرفة من أقسام الاسم، بل هي مؤولة بالنكرة،",
     "en": "It is not far-fetched that the ḥāl which is a clause be counted under “the like of it”; for a clause is not indefinite—since that, like the definite, is among the divisions of the noun—but is reinterpreted as an indefinite;"},
    {"type": "pair",
     "ar": "فجعل العراك ونحوه مصدرا للجملة الحالية المحذوفة إطالة للطريق.",
     "en": "so making al-ʿirāk and its like the maṣdar of an elided circumstantial clause lengthens the way."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "والأصح على قياس تقدير الخبر الظرف بالجملة.",
     "en": "This is soundest by analogy with construing the adverbial predicate as a clause."},
    # REVIEW: print reads «معركة» (the matn has «معتركة»); transcribed as printed.
    {"type": "pair",
     "ar": "ويجوز تقدير الصفة أي: معركة؛ لأن الأصل في الحال الإفراد، فجرى الشارح على مذهب الأكثر.",
     "en": "Supplying an adjective, that is, “muʿtarika” (jostling), is also permitted, because the base of the ḥāl is to be a single word; the commentator followed the doctrine of the majority."},
    {"type": "pair",
     "ar": "ومن لم يتنبه زاد على كلام الشارح حيث قال: الأفعال محذوفة أو صفات، فسوى بينهما.",
     "en": "One who did not notice this added to the commentator’s words, saying: “the verbs are elided, or adjectives,” and so put the two on a par."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "إشارة إلى أن العراك مصدر لم يستعمل فعله، بل استعمل المزيد فيه.",
     "en": "An indication that al-ʿirāk is a maṣdar whose [base] verb is not used; rather, the augmented form is used."},
]
