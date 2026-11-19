# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 322 (printed ٣٢١)."""

PAGE_NUMBER = 322
PRINTED_PAGE = "٣٢١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… أن يقال:» at the foot of PDF p. 321 (mid-sentence).
    {"type": "matn",
     "ar": "«أخي وأبي» مثل: «يدي ودمي» بلا رد المحذوف لجعله نسيا منسيا.",
     "en": "…“akhī” and “abī,” like “yadī” (my hand) and “damī” (my blood), without restoring the elided letter, since it has been made wholly forgotten."},
    {"type": "matn",
     "ar": "(وأجاز المبرد) فيهما: («أخي وأبي») برد لام الفعل فيهما -وهي الواو[[١]]- وجعلها ياء، وإدغام الياء في الياء، وتمسك في ذلك بقول الشاعر:",
     "en": "(Al-Mubarrad allowed) in them (“akhiyya” and “abiyya”), by restoring the final radical (lām al-fiʿl) in both—namely the wāw—turning it into a yāʾ, and assimilating the yāʾ into the yāʾ; he relied for this on the poet’s words:"},
    # The first hemistich is printed only as a row of dots.
    {"type": "verse",
     "ar": "……………      وأبي مالك ذو المجاز[[٢]] بدار",
     "en": "… and by my father, Dhū al-Majāz is no abode for you."},
    {"type": "matn",
     "ar": "وحمل الأخ على الأب، لتقاربهما لفظا ومعنى.",
     "en": "He treated “akh” by analogy with “ab” because of their closeness in form and meaning."},
    {"type": "matn",
     "ar": "فأجاب عنه المصنف في شرحه: بأن ذلك خلاف القياس[[٣]] واستعمال الفصحاء",
     "en": "The author answered this in his commentary [on the Kāfiya]: that it goes against analogy (qiyās) and against the usage of the eloquent,"},
    {"type": "matn",
     "ar": "مع أنه يحتمل[[٤]] أن يكون المقسم به -أي: أبي- جمع أب، فأصله «أبين»[[٥]] سقطت النون بالإضافة فاجتمعت ياآن، فأدغمت الأولى في الثانية، فصار «أبي»،",
     "en": "besides the possibility that what is sworn by—namely “abiyya”—is the plural of “ab”: its original form is “abīna”; the nūn dropped through annexation, two yāʾs met, the first was assimilated into the second, and it became “abiyya.”"},
    {"type": "matn",
     "ar": "وقد جاء جمعه هكذا في قول الشاعر:",
     "en": "Its plural has occurred thus in the poet’s words:"},
    {"type": "verse",
     "ar": "فلما تبين أصواتنا      بكين وفديننا بالأبينا",
     "en": "When they made out our voices, they wept and ransomed us with [their] fathers."},
    {"type": "matn",
     "ar": "أي: لما سمعن وعلمن أصواتنا بكين، وقلن لنا: آباؤنا فداكم.",
     "en": "That is: when they heard and recognized our voices, they wept and said to us: “Our fathers be your ransom.”"},
    {"type": "matn",
     "ar": "(وتقول) أي: امرأة قائلة[[٦]] -لامتناع إضافة «الحم» إلى المذكر- («حمي وهني») بلا رد المحذوف عند الإضافة إلى ياء المتكلم،",
     "en": "(And you say)—that is, a woman speaking, since “al-ḥam” (the husband’s kin) cannot be annexed to a male—(“ḥamī” and “hanī”), without restoring the elided letter on annexation to the yāʾ of the speaker."},
    {"type": "matn",
     "ar": "وإنما فصلهما عن «أخي وأبي»؛ لأنه لم ينقل عن المبرد فيهما في المشهور ما يخالف مذهب الجمهور، وإن نقل عنه بعضهم ذلك الخلاف في الأسماء الأربعة.",
     "en": "He separated them from “akhī” and “abī” only because, in the well-known report, nothing contrary to the doctrine of the majority is transmitted from al-Mubarrad concerning them, though some have transmitted that disagreement from him for all four nouns."},
    {"type": "matn",
     "ar": "(ويقال) في «فم» حال إضافته إلى ياء المتكلم («في») بالرد والقلب والإدغام (في",
     "en": "(And one says) for “fam” (mouth), when it is annexed to the yāʾ of the speaker, (“fiyya”), with restoration, conversion and assimilation, (in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بدليل أخوان وأبوان في حال الرفع وفي حال الجر الياء،",
     "en": "As shown by “akhawāni” and “abawāni” in the nominative, with the yāʾ in the genitive;"},
    {"type": "pair",
     "ar": "فقياس قول المبرد أن يقول في حال النصب إياي.",
     "en": "so the analogy of al-Mubarrad’s view is that he should say “iyyāy” in the accusative."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: خطاب للمؤنث كتب في الحاشية أوله: قدر أحلك ذا المجاز.",
     "en": "It has been said: it is an address to a woman. Its opening was written in the gloss: “qadarun aḥallaki Dhā al-Majāz” (a decree made you settle at Dhū al-Majāz)."},
    {"type": "pair",
     "ar": "وقد أرى قدر أي قضاء.",
     "en": "“And I may think”—qadar meaning decree (qaḍāʾ)."},
    # REVIEW: «اسم سوق بمعنى» as printed; perhaps for «بمنى» (a market at Minā); transcribed as printed.
    {"type": "pair",
     "ar": "وذو المجاز اسم سوق بمعنى.",
     "en": "Dhū al-Majāz is the name of a market, [printed:] “bi-maʿnā.”"},
    {"type": "pair",
     "ar": "ومعنى أرى: أظن، انتهى. وأرى بصيغة المجهول.",
     "en": "The meaning of “arā” is “I suppose”; end [of quotation]. And “urā” is in the passive form."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "على أنه يجوز أن يكون مختصا بضرورة الشعر.",
     "en": "Besides, it may be restricted to poetic necessity."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فلا يصح إثبات مذهب بمجرد الاحتمال.",
     "en": "So a doctrine cannot be established on a mere possibility."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "كأخين جمع أخ.",
     "en": "Like “akhīna,” plural of “akh.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "جعله صيغة غائبة مع أن المتبادر من أمثاله في عبارة المصنفين صيغة الخطاب دفعا لما يتجه أن الصواب وتقولين،",
     "en": "He took it as a third-person feminine form, although what first comes to mind for such expressions in authors’ usage is the second-person form, to fend off the objection that the correct form would be “taqūlīna” (you [fem.] say),"},
    {"type": "pair",
     "ar": "واحترازا عن بعد ما قيل: إن حمي فيه حذف مضاف أي: حم زوجتي،",
     "en": "and to avoid the far-fetched claim that in “ḥamī” an annexed noun is elided, that is, “the ḥam of my wife.”"},
    {"type": "pair",
     "ar": "ولو قال المصنف: «ويقال» لكان أوضح.",
     "en": "Had the author said “and it is said,” it would have been clearer."},
]
