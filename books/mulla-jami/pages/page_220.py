# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 220 (printed ٢١٩)."""

PAGE_NUMBER = 220
PRINTED_PAGE = "٢١٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "على حرفين ليس للترخيم (حذفتا) أي: الحرفان الأخيران في كلا القسمين:",
     "en": "…on two letters is not due to curtailment—(both are dropped), that is, the last two letters, in both categories:"},
    {"type": "matn",
     "ar": "أما في الأول: فلما كانتا في حكم الواحدة، فكما زيدتا معا حذفتا معا.",
     "en": "In the first, since the two are in the status of a single one, they are dropped together just as they were added together."},
    {"type": "matn",
     "ar": "وأما في الثاني: فلأنه لما حذفت الأخير مع صحته وأصالته حذفت المدة الزائدة؛",
     "en": "In the second, it is because, once the last [letter] was dropped despite being sound and a root letter, the added madda was dropped,"},
    {"type": "matn",
     "ar": "لئلا يرد المثل السائر: «صلت على الأسد وبلت عن النقد».",
     "en": "lest the current proverb apply: “I pounced on the lion and fled from the sheep” (ṣultu ʿalā al-asad wa-bultu ʿan al-naqad)."},
    {"type": "matn",
     "ar": "(وإن كان مركبا) ويعلم من بيان شرط الترخيم أنه لا يكون مضافا ولا جملة،",
     "en": "(If it is a compound)—and it is known from the statement of the condition of curtailment that it is neither annexed nor a sentence—"},
    {"type": "matn",
     "ar": "مثل: «بعلبك وخمسة عشر» علمين (حذف الاسم الأخير) فيقال في بعلبك: «يا بعل»، وفي «خمسة عشر»[[١]]: «يا خمسة»[[٢]]،",
     "en": "such as “Baʿlabakk” and “Khamsata ʿAshar” as proper names, (the last noun is dropped): one says for Baʿlabakk “yā Baʿla,” and for “Khamsata ʿAshar” “yā Khamsata,”"},
    {"type": "matn",
     "ar": "لنزوله منزلة تاء التأنيث في كون كل منهما كلمة على حدة، صارت بمنزلة الجزء.",
     "en": "because it stands in the place of the feminine tāʾ, in that each is a separate word that has come to be like a part [of the word]."},
    {"type": "matn",
     "ar": "(وإن كان غير ذلك) المذكور من الأقسام الثلاثة (فحرف واحد[[٣]]) أي: فيحذف حرف واحد، لحصول الفائدة المقصودة، وعدم موجب حذف الأكثر",
     "en": "(If it is other than that)—the three categories mentioned—(then one letter), that is, one letter is dropped, because the intended benefit is obtained and there is nothing requiring more to be dropped,"},
    {"type": "matn",
     "ar": "نحو: «يا حار ويا مال» في «يا حارث ويا مالك».",
     "en": "as in “yā Ḥāru” and “yā Mālu” for “yā Ḥārithu” and “yā Māliku.”"},
    {"type": "matn",
     "ar": "(وهو) أي: المنادى المرخم (في حكم) المنادى (الثابت[[٤]]) لجميع أجزائه، فيبقى الحرف[[٥]] الذي صار آخر الكلمة بعد الترخيم على ما كان عليه قبله (على) الاستعمال",
     "en": "(It)—that is, the curtailed vocative—(is in the status of) a vocative (that retains) all its parts; so the letter that has become the end of the word after curtailment remains as it was before it, (according to) the usage…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: print reads «اثنا عشرة ... واثنتا عشرة» with «اثنتا عشرة» twice; transcribed as printed.
    {"type": "pair",
     "ar": "قالوا: إذا رخمت اثنا عشرة واثنتا عشرة واثني عشر واثنتا عشرة حذفت عشر مع الألف والتاء؛ لأن عشر بمنزلة النون في اثنان.",
     "en": "They said: when you curtail ithnā ʿashrata, ithnatā ʿashrata, ithnay ʿashara and ithnatā ʿashrata, you drop ʿashar together with the alif and the tāʾ, because ʿashar stands in the place of the nūn in ithnān."},
    {"type": "pair",
     "ar": "قال المصنف: وفيه نظر من جهة الثاني اسم برأسه.",
     "en": "The author said: there is a difficulty in this, in that the second is a noun in its own right."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: print reads «ورحمت»; the sense requires «ورخمت» (and you curtailed); transcribed as printed.
    {"type": "pair",
     "ar": "وفي الوقف تقلب التاء هاء كما أنك لو سميت رجلا بمسلمتين ورحمت ووقف قلت: يا مسلمه بالهاء.",
     "en": "In pause the tāʾ changes to hāʾ, just as, if you named a man “Muslimatayn,” curtailed it and paused, you would say “yā Muslimah,” with the hāʾ."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: فالمحذوف حرف واحد أتى هنا بالجملة الاسمية بقرينة الفاء لكون هذا الحذف كثيرا مستمرا.",
     "en": "That is: “then what is dropped is one letter.” He used a nominal sentence here, as the fāʾ indicates, because this elision is frequent and continuous."},
    {"type": "pair",
     "ar": "إن قلت: استمراره تجددي، وهو مستفاد من المضارع لا من الاسمية؟",
     "en": "If you say: its continuity is one of renewal, and that is conveyed by the imperfect verb, not by the nominal sentence?"},
    {"type": "pair",
     "ar": "قلنا: هذا إذا نظر إلى أفراد الحذف. أما إذا نظر إلى نفس الطبيعة فثبوتي.",
     "en": "We say: that holds when one looks at the individual instances of elision; when one looks at the nature itself, it is [continuity] of permanence."},
    {"type": "pair",
     "ar": "والشارح قدس سره نظر إلى الأفراد كما هو المتبادر، وإلى مناسبة المضارع للماضي الواقع جزاء في الشق السابق، فقدر المضارع،",
     "en": "The commentator, may his secret be sanctified, looked to the individual instances, as is what first comes to mind, and to the fit between the imperfect and the perfect that occurs as the apodosis in the preceding alternative; so he supplied the imperfect,"},
    {"type": "pair",
     "ar": "والفاء الجزائية تدخل على المضارع المثبت.",
     "en": "and the fāʾ of the apodosis enters on the affirmative imperfect."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إن قيل: إنما يجعلون المحذوف في حكم الثابت إذا كان الحذف لعلة موجبة، وليس الحذف هنا لعلة موجبة، فينبغي أن يجعل المحذوف فيه كالمحذوف في يد ودم؟",
     "en": "If it is said: they treat the elided as retained only when the elision is due to a necessitating cause, and the elision here is not due to a necessitating cause; so what is elided in it should be treated like what is elided in “yad” and “dam”?"},
    {"type": "pair",
     "ar": "أجيب عنه: بأن المحذوف هنا لعلة قياسية مطردة، فجعلوه كالمحذوف للعلة الموجبة.",
     "en": "It is answered that what is elided here is elided for a regular, analogical cause, so they treated it like what is elided for a necessitating cause."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إلا في مواضع:",
     "en": "Except in certain places:"},
    {"type": "pair",
     "ar": "منها: اسم أزال الترخيم ما يوجب حرف لين منه، فيقال في أعلون وقاضون أعلى وقاضي.",
     "en": "Among them: a noun from which curtailment has removed what necessitated [changing] a soft letter in it; so for “aʿlawn” and “qāḍūn” one says “aʿlā” and “qāḍī.”"},
    {"type": "pair",
     "ar": "ومنها: اسم يبقى بعد المحذوف منه حرف أصلي السكون كان مدغما في ذلك المحذوف، وقبله ألف نحو: أسحار بكسرة الهمزة أو فتحها وهو نبت.",
     "en": "Among them: a noun in which, after the elision, there remains a letter originally quiescent that was assimilated into the elided letter, with an alif before it, as in “isḥārr,” with kasra or fatḥa on the hamza—it is a plant."},
    {"type": "pair",
     "ar": "فسيبويه يفتح الآخر، وغيره يجيز الكسرة أيضا",
     "en": "Sībawayh gives the last [letter] a fatḥa; others also allow the kasra."},
    {"type": "pair",
     "ar": "وإن لم يكن أصلي السكون يرد إلى أصل حركته إن لزم ساكنان نحو: يا راد",
     "en": "If it is not originally quiescent, it is returned to its original vowel if two quiescent letters would otherwise meet, as in “yā Rādi.”"},
    {"type": "pair",
     "ar": "وإن لم يلزم ساكنان، فالنحاة يبقون الساكن على سكونه نحو: يا محمر، والفراء يرد إلى أصل حركته، وهو الكسر.",
     "en": "If two quiescent letters would not meet, the grammarians leave the quiescent letter quiescent, as in “yā Muḥmarr”; al-Farrāʾ returns it to its original vowel, which is the kasra."},
]
