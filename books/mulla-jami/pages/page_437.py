# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 437 (printed ٤٣٦)."""

PAGE_NUMBER = 437
PRINTED_PAGE = "٤٣٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(واللفظي: بخلافه) … أي: ليس بإزائه ذكر» at the foot of PDF p. 436 (mid-sentence).
    {"type": "matn",
     "ar": "من الحيوان، بل تأنيثه منسوب إلى اللفظ، لوجود علامة التأنيث في لفظه حقيقة، أو تقديرا، أو حكما، بلا تأنيث حقيقي في معناه",
     "en": "…of animals; rather, its femininity is ascribed to the wording, because a mark of the feminine is present in its wording, really, by supposition or by legal status, with no real femininity in its meaning,"},
    {"type": "matn",
     "ar": "(كـ«ظلمة») مثال للتأنيث اللفظي حقيقة (و«عين») مثال للتأنيث اللفظي تقديرا، فإن تاء التأنيث مقدرة فيها، بدليل تصغيرها على «عيينة»،",
     "en": "(as in “ẓulma” (darkness)), an example of verbal femininity that is real, (and “ʿayn” (eye)), an example of verbal femininity by supposition, for the feminine tāʾ is supposed in it, as shown by its diminutive “ʿuyayna”."},
    {"type": "matn",
     "ar": "ولم يورد مثالا للمؤنث اللفظي الحكمي كـ«عقرب» لقلة وقوعه.",
     "en": "He gives no example of the verbal feminine by legal status, such as “ʿaqrab” (scorpion), because it rarely occurs."},
    {"type": "matn",
     "ar": "(وإذا أسند الفعل) بلا فصل كما هو الأصل[[١]] (إليه) أي: إلى المؤنث مطلقا حقيقيا ولفظيا ومظهرا أو مضمرا (فبالتاء[[٢]]) أي: فذلك الفعل متلبس بالتاء وجوبا إيذانا بتأنيث الفاعل من أول الأمر،",
     "en": "(When the verb is predicated), without separation, as is the base, (of it), that is, of the feminine absolutely, real or verbal, overt or pronominal, (then with the tāʾ), that is, that verb carries the tāʾ necessarily, to announce the femininity of the agent (fāʿil) from the outset,"},
    {"type": "matn",
     "ar": "إلا إذا كان[[٣]] مسندا إلى ظاهر غير الحقيقي، فإنه حينئذ لك الاختيار في إلحاق التاء[[٤]] وتركه،",
     "en": "except when it is predicated of an overt noun that is not real [feminine]; for then you have the choice of adding the tāʾ or omitting it."},
    {"type": "matn",
     "ar": "وإلى هذا إشارة بقوله: (وأنت في ظاهر غير الحقيقي بالخيار) فهو بمنزلة الاستثناء من هذه القاعدة،",
     "en": "To this he alludes with his words: (and with an overt non-real [feminine] you have the choice); so it stands as an exception to this rule."},
    {"type": "matn",
     "ar": "فلك أن تقول في «طلعت الشمس»: طلع الشمس، بخلاف «الشمس طلعت»، فإنه لا يجوز فيه: «الشمس طلع»؛",
     "en": "So in place of “ṭalaʿat al-shamsu” (the sun rose) you may say “ṭalaʿa al-shamsu”, unlike “al-shamsu ṭalaʿat”, for which “al-shamsu ṭalaʿa” is not allowed,"},
    {"type": "matn",
     "ar": "لكون التأنيث فيه لفظيا، واستغنائه عن إلحاق التاء لما في لفظه من الإشعار به، بخلاف مضمره؛ إذ ليس فيه ما يشعر بتأنيثه.",
     "en": "because the femininity in it is verbal, and because it does without the added tāʾ owing to the indication of it in its wording, unlike its pronoun, since there is nothing in that to indicate its femininity."},
    {"type": "matn",
     "ar": "وجعل بعض الشارحين ضمير «إليه» راجعا إلى المؤنث الحقيقي[[٥]]، أو ضمير المؤنث اللفظي بقرينة قوله: «وأنت في ظاهر غير الحقيقي بالخيار»،",
     "en": "One of the commentators took the pronoun of “ilayhi” as referring to the real feminine, or to the pronoun of the verbal feminine, on the evidence of his words “and with an overt non-real [feminine] you have the choice”."},
    {"type": "matn",
     "ar": "ولو كان يستثنى من هذه القاعدة صورة الفصل أيضا لئلا يحتاج إلى التقييد بقولنا: «بلا فصل» لكان أحسن استيفاء لأحكام جميع الأقسام،",
     "en": "Had the case of separation also been excepted from this rule, so that there were no need for the restriction by our words “without separation”, it would have been a better coverage of the rules of all the kinds;"},
    {"type": "matn",
     "ar": "ففي صورة الفصل أيضا لك الخيار في إلحاق التاء بالفعل، وفي تركه، فتقول: «حضرت القاضي[[٦]] امرأة، وحضر القاضي امرأة،",
     "en": "for in the case of separation too you have the choice of adding the tāʾ to the verb or omitting it, so you say: “ḥaḍarat al-qāḍiya imraʾatun” and “ḥaḍara al-qāḍiya imraʾatun” (a woman came to the judge)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: تبادر قيد بلا فصل من العبارة لأصالته،",
     "en": "He means: the restriction “without separation” is what first comes to mind from the expression, because it is the base."},
    {"type": "pair",
     "ar": "ولا يبعد أن يقال: المتبادر من الفعل أيضا المتصرف، فلا يرد نعم المرأة ونعمت المرأة.",
     "en": "It is not far-fetched to say: what first comes to mind from “the verb” is also the conjugable verb, so “niʿma al-marʾatu” and “niʿmati al-marʾatu” do not count as an objection."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "غالبا؛ لأنه قد ورد حذفها مع ضمير المؤنث الغير الحقيقي نحو: ولا أرض أبقل إبقالها.",
     "en": "Usually; because its omission is attested with the pronoun of a non-real feminine, as in “wa-lā arḍa abqala ibqālahā” (nor any land that brought forth herbs as it did)."},
    {"type": "pair",
     "ar": "وحكى سيبويه عن بعض العرب قال: فلانة.",
     "en": "Sībawayh reported from some of the Arabs [the usage] “qāla fulānatu” (so-and-so [fem.] said)."},
    {"type": "pair",
     "ar": "ووقع في بعض نسخ المتن: فالتاء أي: واجبة.",
     "en": "In some copies of the matn it reads “fa-l-tāʾu”, that is, [the tāʾ is] necessary."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وإلا إذا كان جمعا، فإنه يجيء بيانه بعد بقوله: وحكم ظاهر الجمع إلى آخره، فهو بمنزلة الاستثناء أيضا، فعلى الشارح التعرض لهذا أيضا.",
     "en": "And except when it is a plural, which will be explained later in his words “and the rule of the overt plural…” to the end; that too stands as an exception, so the commentator ought to have addressed this as well."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «أولا» with shadda and tanwīn (awwalan, "first"); the sense seems to require «أو لا» ("or not"). Transcribed as printed (diacritics dropped); translated by the apparent sense.
    {"type": "pair",
     "ar": "وقع فصل أولا. وقد جاء في القرآن ذلك.",
     "en": "Whether separation occurs or not. This occurs in the Qurʾān."},
    {"type": "pair",
     "ar": "وقول بعض النحويين: إن الإتيان بالتاء أحسن ليس سديدا للإجماع في قوله تعالى: ﴿وجمع الشمس والقمر﴾ (القيامة:٩) على التذكير،",
     "en": "The statement of some grammarians that using the tāʾ is better is not sound, given the consensus on the masculine in His words, the Exalted: “and the sun and the moon are brought together” (Qurʾān, Sūrat al-Qiyāma 75:9);"},
    {"type": "pair",
     "ar": "فإذا الأمران متساويان، كذا في الإيضاح.",
     "en": "so the two options are equal; so it is in al-Īḍāḥ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ظاهرا كان أو ضميرا.",
     "en": "Whether overt or pronominal."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أورد المثالين مما فيه الفصل بغير إلا؛ لأن الأجود في صورة الفصل بـ«إلا» ترك التاء في الرافع نحو: ما قام إلا هند.",
     "en": "He gives both examples from cases of separation by something other than “illā”, because in separation by “illā” the better usage is to omit the tāʾ in the governing verb, as in “mā qāma illā Hindun” (none but Hind stood)."},
]
