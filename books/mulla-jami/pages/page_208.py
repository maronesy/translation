# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 208 (printed ٢٠٧)."""

PAGE_NUMBER = 208
PRINTED_PAGE = "٢٠٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "الحقيقة منادى مستقل، فينبغي أن يكون على حالة جارية عليه[[١]] على تقدير مباشرة حرف النداء[[٢]] له، وهي الضمة أو ما يقوم مقامها،",
     "en": "…reality an independent vocative; so it ought to be in the state that would apply to it were the vocative particle supposed to be directly attached to it, namely the ḍamma or what stands in its place;"},
    {"type": "matn",
     "ar": "ولكن لما لم يباشره حرف النداء جعلت تلك الحالة إعرابا، فصارت رفعا.",
     "en": "but since the vocative particle is not directly attached to it, that state was made an inflection (iʿrāb), and so became the nominative."},
    {"type": "matn",
     "ar": "(وأبو عمرو) ابن العلاء النحوي القارئ المقدم على الخليل، يختار فيه (النصب) مع تجويزه الرفع،",
     "en": "(And Abū ʿAmr) ibn al-ʿAlāʾ, the grammarian and Qurʾān reader who preceded al-Khalīl, prefers in it (the accusative), while allowing the nominative;"},
    {"type": "matn",
     "ar": "فإنه لما امتنع فيه تقدير حرف النداء بواسطة اللام لا يكون منادى مستقلا، فله حكم التبعية، وتابع المبني تابع لمحله، ومحله النصب[[٣]].",
     "en": "for since supposing the vocative particle in it is barred on account of the lām, it is not an independent vocative; so it has the rule of following, and the appositive of an indeclinable noun follows its position, and its position is accusative."},
    {"type": "matn",
     "ar": "(وأبو العباس) المبرد (إن كان) المعطوف المذكور (كالحسن) أي: كاسم الحسن في جواز نزع اللام عنه[[٤]] (فكالخليل)",
     "en": "(And Abū al-ʿAbbās) al-Mubarrad: (if) the said coordinated noun (is like al-Ḥasan)—that is, like the name al-Ḥasan in that the lām may be stripped from it—(then [he is] like al-Khalīl),"},
    {"type": "matn",
     "ar": "أي: فأبو العباس مثل الخليل في اختيار رفعه؛ لإمكان جعله منادى مستقلا بنزع اللام عنه",
     "en": "that is, Abū al-ʿAbbās is like al-Khalīl in preferring its nominative, since it can be made an independent vocative by stripping the lām from it;"},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن المعطوف المذكور كاسم الحسن في جواز نزع اللام عنه مثل: «النجم والصعق» (فكأبي عمرو)",
     "en": "(otherwise)—that is, if the said coordinated noun is not like the name al-Ḥasan in that the lām may be stripped from it, such as “al-Najm” and “al-Ṣaʿiq”—(then [he is] like Abū ʿAmr),"},
    {"type": "matn",
     "ar": "أي: أبو العباس مثل أبي عمرو في اختيار النصب؛ لامتناع جعله منادى مستقلا.",
     "en": "that is, Abū al-ʿAbbās is like Abū ʿAmr in preferring the accusative, since it cannot be made an independent vocative."},
    {"type": "matn",
     "ar": "(والمضافة[[٥]]) عطف على «المفردة»[[٦]]، أي: وتوابع المنادى المبني على ما يرفع به المضافة بالإضافة الحقيقية (تنصب)؛",
     "en": "(And the annexed ones) is coordinated with “the singular ones” (al-mufrada), that is: the appositives of a vocative built on what marks its nominative, when they are annexed by genuine annexation, (take the accusative);"},
    {"type": "matn",
     "ar": "لأنها إذا وقعت منادى تنصب[[٧]]، فنصبها إذا",
     "en": "because when they occur as a vocative they take the accusative; so their accusative, when…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أنه لو باشر المضاف بالإضافة اللفظية أو شبه المضاف حرف النداء لكان منصوبا، فينبغي ألا يختار فيهما الرفع.",
     "en": "Against this: had the vocative particle been directly attached to a noun annexed by verbal annexation (iḍāfa lafẓiyya), or to one resembling the annexed, it would be accusative; so the nominative ought not to be preferred in these two."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أنه على هذا ينبغي أن يكون المعطوف الذي هو مضاف بالإضافة اللفظية أو مشابه به منصوبا عند الخليل.",
     "en": "Against this: on this [reasoning], the coordinated noun that is annexed by verbal annexation, or resembles the annexed, ought to be accusative according to al-Khalīl."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أنه على هذا ينبغي أن يكون المختار النصب عند أبي عمرو في سائر التوابع أيضا، فلا وجه للتخصيص بالمعطوف المذكور.",
     "en": "Against this: on this [reasoning], the accusative ought to be the preferred option for Abū ʿAmr in all the other appositives too; so there is no ground for restricting it to the said coordinated noun."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فسر العلم الذي يجوز نزع اللام عنه بالمعرف باللام الذي قصد بلامه التعريف أو جعل لامه جزء العلم.",
     "en": "The proper name (ʿalam) from which the lām may be stripped has been explained as one made definite by the lām whose lām is meant for definiteness, or whose lām has been made part of the proper name."},
    {"type": "pair",
     "ar": "وذلك يكون في علم هو اسم جنس في الأصل، خص بفرد منه بخاصة له اقتضت ذلك التخصيص، ويسمى علما غالبا.",
     "en": "This occurs in a proper name that was originally a generic noun, restricted to one individual of its kind by a peculiarity of his that called for that restriction; it is called a prevalent proper name (ʿalam ghālib)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: بالإضافة المعنوية.",
     "en": "That is: by semantic annexation (iḍāfa maʿnawiyya)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وتنصب على ترفع عطف أمرين على معمولي عامل واحد؛ لأن العامل في صفة المبتدأ والخبر واحد هو الابتداء.",
     "en": "And “tunṣabu” [is coordinated] with “turfaʿu”: a coordination of two things with the two governed terms of a single governor; because the governor in the qualifier of the mubtadaʾ and in the khabar is one, namely inception (al-ibtidāʾ)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فيه أن هذا الدليل يقتضي ألا فرق بين المضاف بالإضافة الحقيقية واللفظية، والمشابه للمضاف؛ لأنه يجري في جميعها",
     "en": "Against this: this proof entails that there is no difference between what is annexed by genuine annexation, by verbal annexation, and what resembles the annexed, since it applies to all of them;"},
    {"type": "pair",
     "ar": "مع أنه أدخل المضاف بالإضافة اللفظية والمشبه بالمضاف في المفرد الذي حكمه جواز الرفع والنصب.",
     "en": "yet he included what is annexed by verbal annexation and what resembles the annexed under the singular, whose rule is that both nominative and accusative are allowed."},
]
