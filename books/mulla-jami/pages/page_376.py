# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 376 (printed ٣٧٥)."""

PAGE_NUMBER = 376
PRINTED_PAGE = "٣٧٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(و«تي») بقلب» at the foot of PDF p. 375.
    {"type": "matn",
     "ar": "ألف ياء[[١]] (و«ته» و«ذه») بقلب الألف والياء[[٢]] هاء[[٣]] بغير وصل الياء بها (و«تهي» و«ذهي») بوصل الياء[[٤]] بها.",
     "en": "…the alif [of “tā”] into a yāʾ; (and “tih” and “dhih”), by changing the alif and the yāʾ into a hāʾ, without joining a yāʾ to it; (and “tihī” and “dhihī”), by joining a yāʾ to it."},
    {"type": "matn",
     "ar": "(ولمثناه) أي: لمثنى المؤنث («تان») في الرفع (و«تين») في النصب والجر،",
     "en": "(For its dual), that is, for the feminine dual, (“tāni”) in the nominative (and “tayni”) in the accusative and genitive;"},
    {"type": "matn",
     "ar": "ولا يثنى من لغاته[[٥]] إلا «تا» لكثرة دورها على الألسنة،",
     "en": "and of its dialectal forms only “tā” is put in the dual, because of how often it circulates on tongues."},
    {"type": "matn",
     "ar": "وتوهم بعضهم من اختلاف أواخر «ذان وذين، وتان وتين» باختلاف العوامل أنها معربة،",
     "en": "Some imagined, from the variation of the endings of “dhāni / dhayni” and “tāni / tayni” with the variation of the governors, that they are declinable (muʿrab);"},
    {"type": "matn",
     "ar": "والجمهور على أن هذا الاختلاف ليس بسبب اختلاف العوامل، بل «ذان وتان» موضوعان لتثنية المرفوع، و«ذين وتين» لتثنية المنصوب والمجرور،",
     "en": "but the majority hold that this variation is not caused by the variation of the governors; rather, “dhāni” and “tāni” are coined for the nominative dual, and “dhayni” and “tayni” for the accusative and genitive dual,"},
    {"type": "matn",
     "ar": "ووقوعها على صورة المعرب اتفاقي، لا لقصد الإعراب لوجود علة البناء فيها.",
     "en": "and their occurring in the form of declinable words is coincidental, not because inflection is intended, since the cause of indeclinability is present in them."},
    {"type": "matn",
     "ar": "(ولجمعهما) أي: جمع المذكر والمؤنث («أولاء» مدا وقصرا) أي: ممدودا ومقصورا وإذا كان مقصورا يكتب بالياء[[٦]].",
     "en": "(For the plural of both), that is, the plural of masculine and feminine, (“ulāʾi”, with madd and with qaṣr), that is, with the long final alif and hamza, and with the short final alif; when it has the short form it is written with yāʾ."},
    {"type": "matn",
     "ar": "(ويلحقها) أي: أسماء الإشارة، يعني: يدخل على أوائلها على سبيل اللحوق[[٧]] والعروض بعد اعتبار أصالتها (حرف التنبيه) وهي كلمة «ها»،",
     "en": "(There attaches to them), that is, to the demonstrative nouns — he means: there enters upon their beginnings, by way of attachment and accidental occurrence after their being regarded as original — (the particle of alerting) (ḥarf al-tanbīh), which is the word “hā”."},
    # REVIEW: «فهي ليس» printed (one would expect «ليست»); transcribed as printed.
    {"type": "matn",
     "ar": "فهي ليس في الحقيقة منها[[٨]]، وإنما هي حرف جيء به للتنبيه على المشار إليه قبل لفظه، كما جيء به للتنبيه",
     "en": "So it is not in reality part of them; it is only a particle brought in to alert [the hearer] to the thing pointed to before its word, just as it is brought in to alert…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن الياء قد تكون علامة للتأنيث، نحو: تضربين.",
     "en": "For the yāʾ is sometimes a sign of the feminine, as in “taḍribīna” (you [f.] strike)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: الألف من ذا والياء من ذي فالأظهر أو الياء.",
     "en": "That is, the alif of “dhā” and the yāʾ of “dhī”; so the more evident [wording] is “or the yāʾ”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن الهاء قد تكون مبدلة من تاء التأنيث في الوقف.",
     "en": "Because the hāʾ is sometimes substituted for the feminine tāʾ in pause (waqf)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الحاصل من الإشباع، أو من إبدال الألف بالهاء والياء معا.",
     "en": "[The yāʾ] that results from prolongation (ishbāʿ), or from replacing the alif with the hāʾ and the yāʾ together."},
    {"type": "pair",
     "ar": "قال عبد الغفور: لحصولها من الإشباع أو الجمع بين العوضين.",
     "en": "ʿAbd al-Ghafūr said: because it arises from prolongation, or from combining the two substitutes."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لا يورد على صورة المثنى، وإلا فلا تثنية في المعنى،",
     "en": "That is, it is not brought in the form of the dual; otherwise there is no dual in meaning,"},
    # REVIEW: «لأنه المعرفة» printed (one would expect «لأن المعرفة», as in ʿAbd al-Ghafūr's wording below); transcribed as printed.
    {"type": "pair",
     "ar": "بل اللفظ بتمامه موضوع لمعنيين، ولو كان مثنى لم يكن في مفهومه تعيين؛ لأنه المعرفة لا تثنى إلا بعد التنكير.",
     "en": "rather, the word as a whole is coined for two referents; and were it a dual, there would be no determinateness in its concept, because a definite noun is put in the dual only after being made indefinite."},
    {"type": "pair",
     "ar": "قال عبد الغفور: لم ترد التثنية المتعارفة؛ لأن المعرفة لا تثنى إلا إذا نكرت، ولا ينكر اسم الإشارة.",
     "en": "ʿAbd al-Ghafūr said: the customary dual is not meant, because a definite noun is put in the dual only when it is made indefinite, and a demonstrative noun is not made indefinite."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لأنه كذا حال الألف المجهول أصله.",
     "en": "Because such is the case of an alif whose origin is unknown."},
    {"type": "pair",
     "ar": "ولذا كتب فيه الواو لئلا يلتبس أولى بـ«إلى» حرف جر، ولا يكتب بالألف الممدودة إذا اتصل به كاف الخطاب،",
     "en": "Hence the wāw is written in it, lest “ulā” be confused with “ilā”, the preposition; and it is not written with the tall alif when the kāf of address is joined to it."},
    {"type": "pair",
     "ar": "ولا يظن أنها تكتب بالياء في أولئك؛ لأن المكتوب في مركز الهمزة.",
     "en": "It should not be thought that it is written with yāʾ in “ulāʾika”, because what is written there is the seat of the hamza."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني: أن اللحوق يقتضي اعتبار أصل أولا، ولا يلزم أن يكون اتصالا بالآخر.",
     "en": "He means: attachment requires that something original be regarded first, and it need not be a joining at the end."},
    {"type": "pair",
     "ar": "وإنما اختار هذه العبارة لدفع ما قد يتوهم أنها جزء اسم الإشارة.",
     "en": "He chose this wording only to repel what might be imagined, namely that it is part of the demonstrative noun."},
    {"type": "pair",
     "ar": "اعلم أنه قد يفصل بين هاء التنبيه واسم الإشارة المجرد عن اللام والكاف.",
     "en": "Know that the hāʾ of alerting is sometimes separated from a demonstrative noun that is bare of the lām and the kāf."},
    {"type": "pair",
     "ar": "وذلك بـ«أنا» وأخواته كثير نحو: ها أنا ذا وها أنتم أولاء، وها هو ذا، وبغيرها قليل.",
     "en": "That [separation] by “anā” and its sisters is frequent, as in “hā anā dhā” (here I am), “hā antum ulāʾi” (here you are) and “hā huwa dhā” (here he is); by other words it is rare."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "يعني: من فوائد كلمة اللحوق التنبيه على أنها ليست في الحقيقة منها على ما يوهمه شدة الامتزاج وكتابته كحروف الكلمة،",
     "en": "He means: among the benefits of the word “attachment” is to alert that it is not in reality part of them, contrary to what the close fusion and its being written like the letters of the word suggest."},
    {"type": "pair",
     "ar": "ولم يقل: ويتصل بها لئلا يوهم عدم جواز الفصل بينها، وذا مع أنه لكلمة أنا",
     "en": "He did not say “and is joined to them”, lest it suggest that separation between them is not permitted; this, although the word “anā”…"},
]
