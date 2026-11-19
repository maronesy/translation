# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 522 (printed ٥٢١)."""

PAGE_NUMBER = 522
PRINTED_PAGE = "٥٢١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 521 ends with a complete sentence (the examples of أصبح / أمسى / أضحى).
    {"type": "matn",
     "ar": "فالمثال الأول يدل على اقتران مضمون الجملة، وهو قيام زيد بوقت الصباح، وعلى هذا القياس المثالان الأخيران.",
     "en": "So the first example indicates the conjunction of the content of the sentence, namely Zayd’s standing, with the time of morning; and the last two examples are on the same analogy."},
    {"type": "matn",
     "ar": "(و) تكون (بمعنى «صار») نحو: «أصبح -أو أمسى، أو أضحى- زيد غنيا» أي: صار،",
     "en": "(And) they are (in the sense of “ṣāra”), as in “aṣbaḥa (or amsā, or aḍḥā) Zaydun ghaniyyan” (Zayd became rich), that is, “ṣāra”;"},
    {"type": "matn",
     "ar": "وليس المراد أنه صار في الصباح أو المساء أو الضحى على هذه الصفة.",
     "en": "what is meant is not that he came to have this attribute in the morning, the evening or the forenoon."},
    {"type": "matn",
     "ar": "(و) تكون (تامة) بمعنى الدخول في هذه الأوقات، تقول: «أصبح زيد» إذا دخل في الصباح.",
     "en": "(And) they are (complete), in the sense of entering these times; you say “aṣbaḥa Zaydun” when he has entered upon the morning."},
    {"type": "matn",
     "ar": "(و«ظل» و«بات»[[١]] لاقتران مضمون الجملة بوقتيهما) فإذا قلت: «ظل زيد سائرا» فمعناه: ثبت له ذلك في جميع نهاره[[٢]]،",
     "en": "(And “ẓalla” and “bāta” are for the conjunction of the content of the sentence with their two times); so when you say “ẓalla Zaydun sāʾiran” (Zayd kept travelling all day), its meaning is that this held of him throughout his day;"},
    {"type": "matn",
     "ar": "وإذا قلت: «بات زيد سائرا» فمعناه: ثبت له ذلك في جميع ليله.",
     "en": "and when you say “bāta Zaydun sāʾiran” (Zayd kept travelling all night), its meaning is that this held of him throughout his night."},
    {"type": "matn",
     "ar": "(وبمعنى «صار») نحو: «ظل زيد غنيا»، و«بات عمرو فقيرا» أي: صار.",
     "en": "(And in the sense of “ṣāra”), as in “ẓalla Zaydun ghaniyyan” (Zayd became rich) and “bāta ʿAmrun faqīran” (ʿAmr became poor), that is, “ṣāra”."},
    {"type": "matn",
     "ar": "وقد يجيء هذان الفعلان تامين أيضا نحو: «ظللت بمكان كذا، وبت مبيتا طيبا»،",
     "en": "These two verbs also sometimes occur as complete, as in “ẓaliltu bi-makān kadhā” (I spent the day in such-and-such a place) and “bittu mabītan ṭayyiban” (I spent a pleasant night);"},
    {"type": "matn",
     "ar": "لكن لما كان مجيئهما تامين في غاية القلة جعله في حكم العدم، ولذلك لم يذكرهما تامتين، وفصلهما عن الأفعال الثلاثة السابقة.",
     "en": "but since their occurrence as complete is extremely rare, he treated it as non-existent; for that reason he did not mention them as complete, and separated them from the three preceding verbs."},
    {"type": "matn",
     "ar": "و«آض، وغدا، وعاد، وراح» فهذه الأفعال[[٣]] الأربعة ناقصة إذا كانت بمعنى: «صار»،",
     "en": "And “āḍa”, “ghadā”, “ʿāda” and “rāḥa”: these four verbs are incomplete when they are in the sense of “ṣāra”,"},
    {"type": "matn",
     "ar": "وتامة في مثل قولك: «آض -أو عاد- زيد من سفره» أي: رجع، و«غدا» إذا مشى في وقت الغداة، و«راح» إذا مشى في وقت الرواح، وهو ما بعد الزوال إلى الليل.",
     "en": "and complete in such a saying of yours as “āḍa (or ʿāda) Zaydun min safarihi” (Zayd returned from his journey), that is, “rajaʿa”; and “ghadā” when he set out at the time of early morning (ghadāh), and “rāḥa” when he set out at the time of rawāḥ, which is from the sun’s decline until night."},
    {"type": "matn",
     "ar": "وأسقط المصنف ذكر هذه الأفعال الأربعة من البين في مقام التفصيل مع ذكرها في مقام الإجمال،",
     "en": "The author dropped mention of these four verbs from the discussion in the place of detailed exposition, although he mentioned them in the place of summary statement;"},
    {"type": "matn",
     "ar": "وكان الوجه في ذلك أنها من الملحقات، ولذا لم يذكرها صاحب المفصل.",
     "en": "the reason for this was that they are among the appended verbs, and for this reason the author of al-Mufaṣṣal did not mention them."},
    {"type": "matn",
     "ar": "وقال صاحب اللباب: وألحق بها «آض، وعاد، وغدا، وراح»، فأسقطها عن",
     "en": "The author of al-Lubāb said: “Appended to them are ‘āḍa’, ‘ʿāda’, ‘ghadā’ and ‘rāḥa’”; so he dropped them from…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «مضارع» at the head of the note, although what follows lists the verbal nouns (بياتا، مبيتا، بيتوتة); likewise «ومضارع «ظل يظل»». Transcribed as printed.
    {"type": "pair",
     "ar": "مضارع «بات يبيت ويبات بياتا ومبيتا وبيتوتة» بمعنى الكون في جميع الليل،",
     "en": "The imperfect of “bāta, yabītu and yabātu, bayātan, mabītan and baytūtatan”, meaning being [in a state] throughout the night;"},
    {"type": "pair",
     "ar": "ومضارع «ظل يظل» بفتح العين «ظلا وظلولا» بمعنى: الكون في جميع النهار.",
     "en": "and the imperfect of “ẓalla yaẓallu”, with fatḥa on the middle radical, “ẓallan and ẓulūlan”, meaning being [in a state] throughout the day."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في الزمان الماضي تركه؛ لأن الكلام في المعاني المخصوصة.",
     "en": "That is, [the phrase] “in past time”: he left it out, because the discussion concerns the specific meanings."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الظاهر ترك الفاء، ولعله بتقدير إما لتفصيل ما أجمله سابقا في المتن،",
     "en": "The apparent [course] would be to omit the fāʾ; perhaps it is on the supposition of “ammā”, for detailing what he stated summarily earlier in the matn;"},
    {"type": "pair",
     "ar": "وإما إعادة هذه الأفعال الأربعة فلتأكيد كون كل واحد منها بمعنى صار.",
     "en": "as for the repetition of these four verbs, it is to emphasize that each of them is in the sense of “ṣāra”."},
]
