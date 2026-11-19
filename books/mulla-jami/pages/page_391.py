# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 391 (printed ٣٩٠)."""

PAGE_NUMBER = 391
PRINTED_PAGE = "٣٩٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وأن صيغتها مخالفة لصيغ الأفعال، وأنها لا» at the foot of PDF p. 390.
    {"type": "matn",
     "ar": "تتصرف تصرفها، لا أنها موضوعة لصيغ الأفعال على أن يكون «رويد» مثلا موضوعا لكلمة «أمهل».",
     "en": "…inflect as they do; not that they were coined for the forms of the verbs, so that “ruwayda”, for example, would be coined for the word “amhil” (give respite)."},
    {"type": "matn",
     "ar": "قال الشارح الرضي: وليس ما قال بعضهم: إن «صه» مثلا اسم للفظ «اسكت» الذي هو دال على معنى الفعل، فهو علم للفظ الفعل لا لمعناه بشيء؛",
     "en": "The commentator al-Raḍī said: what some have said is of no account, namely that “ṣah”, for example, is a name for the expression “uskut” (be silent), which signifies the meaning of the verb, so that it is a proper name for the verb’s expression, not for its meaning;"},
    {"type": "matn",
     "ar": "إذ العربي القح[[١]] ربما يقول: «صه» مع أنه لم يخطر بباله لفظ «اسكت»، وربما لم يسمعه أصلا»،",
     "en": "for the pure-blooded Arab may say “ṣah” although the expression “uskut” never crossed his mind, and he may never have heard it at all.”"},
    {"type": "matn",
     "ar": "ولهذا قال المصنف: «ما كان بمعنى الأمر أو الماضي»، ولم يقل: ما كان معناه الأمر أو الماضي،",
     "en": "For this reason the author said “what is in the sense of the imperative or the past”, and did not say “what has as its meaning the imperative or the past”."},
    {"type": "matn",
     "ar": "والمتبادر أن يكون هذا بحسب الوضع[[٢]]، فلا يرد مثل: «الضارب أمس»[[٣]] نقضا على التعريف.",
     "en": "What first comes to mind is that this is by coinage (waḍʿ); so such as “al-ḍāribu amsi” (the one who struck yesterday) is not an objection to the definition."},
    {"type": "matn",
     "ar": "(و«فعال») أي: ما يوزن بـ«فعال» الكائن (بمعنى الأمر) المشتق (من الثلاثي[[٤]]) المجرد (قياس) أي: قياسي[[٥]] (كـ«نزال» بمعنى انزل)",
     "en": "(And “faʿāli”), that is, what is on the measure “faʿāli”, being (in the sense of the imperative) and derived (from the triliteral) unaugmented [verb], (is regular) (qiyās), that is, formed by analogy, (like “nazāli” in the sense of “inzil” (dismount))."},
    {"type": "matn",
     "ar": "قال سيبويه: هو مطرد في الثلاثي المجرد.",
     "en": "Sībawayh said: it is regular in the unaugmented triliteral."},
    {"type": "matn",
     "ar": "ويرد عليه: أنه لا يقال: «قوام وقعاد» في «قم واقعد»، فلهذا تأول بعضهم قول سيبويه: بأنه أراد بالاطراد الكثرة، فكأنه قياس لكثرته،",
     "en": "Against him it is objected that one does not say “qawāmi” and “qaʿādi” for “qum” (stand) and “uqʿud” (sit); so some interpreted Sībawayh’s statement to mean that by regularity he meant frequency, so that it is as if regular because of its frequency."},
    {"type": "matn",
     "ar": "وأما في الرباعي فاتفقوا على أنه لم يأت[[٦]] إلا نادرا.",
     "en": "As for the quadriliteral, they agree that it has occurred only rarely."},
    {"type": "matn",
     "ar": "(و«فعال») حال كونه (مصدرا[[٧]] معرفة[[٨]]، كـ«فجار»[[٩]]) بمعنى: الفجرة أو الفجور.",
     "en": "(And “faʿāli”) when it is (a definite maṣdar, like “fajāri”), in the sense of al-fajra or al-fujūr (wickedness)."},

    {"type": "rule"},

    # ---------------- Footnote continued from the previous page ----------------
    # Continuation of fn. ٥ of PDF p. 390 («...فمعنى «صه» بلا»).
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "تنوين اسكت السكوت المعهود المعين، وتعيين المصدر بتعيين متعلقه أي: المسكوت عنه.",
     "en": "…nunation is “keep the known, specific silence”; the maṣdar is made specific by making specific what it relates to, that is, what one is to be silent about."},
    {"type": "pair",
     "ar": "فحاصله: افعل السكوت عن هذا الحديث، فجاز ألا يسكت المخاطب عن غير هذا الحديث، ومعنى صه بالتنوين اسكت سكوتا ما.",
     "en": "Its upshot is “be silent about this talk”, so the one addressed may not be silent about other than this talk; while the meaning of “ṣahin” with nunation is “be silent with some silence”."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في الحاشية: القح الخالص. وفي القاموس: القح بالضم الخالص من اللوم.",
     "en": "In the Ḥāshiya: al-quḥḥ is the pure. In al-Qāmūs: al-quḥḥ, with ḍamma, is the one free of blame."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وإن كان طاريا.",
     "en": "Even if it is incidental."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لو قال: بدل أمس في الماضي لكان أظهر.",
     "en": "Had he said “in the past” instead of “amsi”, it would have been clearer."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أن قوله من الثلاثي صفة لأمر. ولا يخفى أن تقدير المشتق أليق من تقدير الكائن.",
     "en": "He means that his words “from the triliteral” qualify “imperative”. It is not hidden that supposing “derived” is more fitting than supposing “being”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: ذو قياس.",
     "en": "That is: subject to analogy."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: على أن اسم الفعل من الرباعي بمعنى الأمر لم يأت إلا نادرا، وهو كلمتان قرقار أي: صوت من التصويت، وعرعار أي: تلاعبوا بالعرعرة وهي لعبة للصبيان.",
     "en": "That is, [they agree] that the verbal noun from the quadriliteral in the sense of the imperative has occurred only rarely; it is two words: “qarqāri”, that is, “make a sound”, and “ʿarʿāri”, that is, “play ʿarʿara”, a children’s game."},
    {"type": "pair",
     "ar": "وقال المبرد: قرقار حكاية صوت الرعد، وعرعار حكاية صوت الصبيان.",
     "en": "Al-Mubarrad said: “qarqār” imitates the sound of thunder, and “ʿarʿār” imitates the voices of children."},
    {"type": "pair",
     "ar": "وفيه أن الحكاية لا تغير فلو كانا صوتين لقيل قارقار وعارعار كغاق غاق.",
     "en": "Against this: imitation is not altered, so had they been sounds one would say “qārqār” and “ʿārʿār”, like “ghāq ghāq”."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "صاحبها ضمير قوله مبني.",
     "en": "The one to which it [the ḥāl] refers is the pronoun in his word “indeclinable”."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: علم جنس كسبحان.",
     "en": "That is, a generic proper name (ʿalam jins), like “subḥāna”."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "صفة أخرى لمصدر. ويجوز أن يكون خبر مبتدأ محذوف، أي: هو كفجار، والجملة معترضة.",
     "en": "A further qualifier of “maṣdar”. It may also be the predicate of an elided subject, that is, “it is like fajāri”, the sentence being parenthetical."},
]
