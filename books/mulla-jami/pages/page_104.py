# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 104 (printed ١٠٣)."""

PAGE_NUMBER = 104
PRINTED_PAGE = "١٠٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(فقدم) وهو مؤنث معنوي سماعي باعتبار معناه الجنسي إذا سمي به رجل (منصرف)؛",
     "en": "(“So ‘qadam’ [foot]”) — which is semantically feminine by transmission (samāʿī), in view of its generic meaning — when a man is named with it, is (“fully declinable”);"},
    {"type": "matn",
     "ar": "لأن التأنيث الأصلي زال بالعلمية للمذكر، من غير أن يقوم شيء مقامه، والعلمية وحدها لا تمنع الصرف.",
     "en": "because the original feminine gender lapses through [the word's] proper-namehood for a male, without anything taking its place; and proper-namehood alone does not prevent declension."},
    {"type": "matn",
     "ar": "(وعقرب) وهو مؤنث معنوي سماعي باعتبار معناه الجنسي إذا سمي به رجل (ممتنع) صرفها؛",
     "en": "(And “ʿaqrab” [scorpion]) — which [too] is semantically feminine by transmission, in view of its generic meaning — when a man is named with it, (its declension is prevented);"},
    {"type": "matn",
     "ar": "لأنه وإن زال التأنيث بالعلمية للمذكر، فالحرف الرابع قائم مقامه،",
     "en": "because, even though the feminine gender lapses through [its] proper-namehood for a male, the fourth letter stands in its place,"},
    {"type": "matn",
     "ar": "بدليل أنه إذا صغر «قدم» ظهر التاء المقدرة، كما يقتضيه قاعدة التصغير[[١]]، فيقال: «قديمة»،",
     "en": "as evidenced by the fact that when “qadam” is made diminutive, the implicit tāʾ appears — as the rule of the diminutive requires[[١]] — so one says “qudayma”;"},
    {"type": "matn",
     "ar": "بخلاف «عقرب»، فإنه إذا صغر يقال: «عقيرب» من غير إظهار التاء[[٢]]؛ لأن الحرف الرابع قائم مقامه،",
     "en": "unlike “ʿaqrab,” for when it is made diminutive one says “ʿuqayrib,” without the tāʾ appearing[[٢]] — because the fourth letter stands in its place;"},
    {"type": "matn",
     "ar": "ف«عقرب» إذا سمي به رجل امتنع صرفه للعلمية والتأنيث الحكمي[[٣]].",
     "en": "so “ʿaqrab,” when a man is named with it, is prevented from declension on account of proper-namehood and the ruled [i.e., constructive] feminine gender (al-taʾnīth al-ḥukmī)[[٣]]."},

    {"type": "section", "ar": "[ المعرفة ]",
     "en": "Definiteness"},

    {"type": "matn",
     "ar": "(المعرفة) أي: التعريف[[٤]]؛ لأن سبب منع الصرف هو وصف التعريف لا ذات المعرفة.",
     "en": "(“Definiteness,” al-maʿrifa) — that is: [the quality of] being made definite (al-taʿrīf)[[٤]] — because the cause of preventing declension is the attribute of definiteness, not the definite entity itself."},
    {"type": "matn",
     "ar": "(شرطها) أي: شرط تأثيرها في منع الصرف: (أن تكون علمية[[٥]]) أي: تكون هذا النوع من جنس التعريف على أن تكون الياء مصدرية، أو منسوبة[[٦]] إلى العلم، بأن",
     "en": "(“Its condition”) — that is: the condition for its having effect in preventing declension — is (“that it be proper-name definiteness,” ʿalamiyya[[٥]]) — that is: that this type be of the genus of definiteness [via a proper name], on the reading that the yāʾ [of ʿalamiyya] is that of a verbal noun (maṣdariyya), or [that it is] a relative yāʾ relating [it][[٦]] to “the proper name” (al-ʿalam), in that…"},  # continues on the next page

    {"type": "rule"},

    # ---------------- Orphan continuation (tail of a footnote from p.103) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "بالجمع. وثالثها: ألا يغلب استعماله بحسب معناه الجنسي في المذكر.",
     "en": "…as “the collective (al-jamʿ).” The third: that its use, in respect of its generic meaning, not predominate for the masculine."},
    {"type": "pair",
     "ar": "ثم أن تساوى استعماله مذكرا ومؤنثا، فتساوى الصرف ومنعه. وإن غلب استعماله مؤنثا، فمنع الصرف راجح. وإن لم يستعمل إلا مؤنثا، فمنع الصرف واجب.",
     "en": "Then: if its use as masculine and as feminine is equal, then declining it and preventing [its declension] are equal; if its use as feminine predominates, then preventing declension is preferable; and if it is used only as feminine, then preventing declension is obligatory."},
    {"type": "pair",
     "ar": "والسر في اشتراط الأولين أن التأنيث المذكور في الأول بقسميه طارئة، وفي الثاني بعارض تأويل غير لازم، وقد زال بالعلمية ما طرأ وما عرض، فلم يبق التأنيث.",
     "en": "The secret behind stipulating the first two [conditions] is that the feminine gender mentioned — in the first, in both of its kinds, is incidental (ṭāriʾa), and in the second is [only] through the accident of a non-necessary construal; and proper-namehood removes whatever is incidental or accidental, so the feminine gender does not remain."},
    {"type": "pair",
     "ar": "والسر في اشتراط الثالث أن الحكم للغالب. ومما ذكرنا يظهر وجه ترك الشروط.",
     "en": "And the secret behind stipulating the third is that the ruling goes by what predominates. From what we have mentioned, the reason for [the author's] omitting these conditions becomes clear."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: من رد الأشياء إلى أصولها.",
     "en": "That is: [it consists] in restoring things to their original [forms]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "في تصغيره لئلا يلزم اجتماع النائب والمنوب عنه.",
     "en": "In its diminutive, lest the substitute (al-nāʾib) and that for which it substitutes come together."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهو الحرف الرابع؛ لأنه في حكم تاء التأنيث.",
     "en": "which is the fourth letter, because it is under the ruling of the feminine tāʾ."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يجوز أيضا أن يقدر المضاف، أي: تعريف المعرفة وأن تعتبر الحيثية، أي: المعرفة من حيث إنها معرفة.",
     "en": "It is also permissible to posit an [omitted] governed term (muḍāf) — that is: “the definiteness of the definite (taʿrīf al-maʿrifa)” — and to take into account the [specific] aspect — that is: the definite inasmuch as it is definite."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: لم يقل شرطه علمية؛ لأن المراد بالمعرفة التعريف، وهو ليس علما.",
     "en": "It has been said: he did not say “its condition is proper-namehood (ʿalamiyya)” [as a predicate of “definiteness”] because what is meant by “definiteness” is [the quality of] making definite, and that is not [itself] a proper name."},
    {"type": "pair",
     "ar": "إن قلت: يجوز أن يراد ما فيه التعريف كما أراد في قوله: التأنيث بالتاء، شرطه العلمية علمية ما فيه التأنيث؟",
     "en": "If you say: it may be that what is intended is “that in which definiteness resides,” just as, in his statement “feminization by the tāʾ, its condition is proper-namehood,” he intended the proper-namehood of that in which the feminization resides?"},
    {"type": "pair",
     "ar": "قلنا: هناك لام أبدل عن المضاف إليه، وليس هنا لام.",
     "en": "We say: there [in that case] there is a lām standing in for the [omitted] second term of the construct (al-muḍāf ilayhi), whereas here there is no lām."},
    {"type": "pair",
     "ar": "إن قلت: لم لم يأت باللام ههنا حتى يكون أخصر؟ قلنا: للزوم التكرار لفظا.",
     "en": "If you say: why did he not bring the lām here, so as to be more concise? We say: because it would entail verbal repetition."},
    {"type": "pair",
     "ar": "إن قلت: فيلزم التكرار في اشتراط العجمة؟ قلنا: لا لزيادة قوله: في العجمية.",
     "en": "If you say: then repetition would [likewise] be entailed in [his] stipulating non-Arab origin? We say: no, because of the addition of his words “in [the case of] non-Arab origin (fī al-ʿujmiyya).”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بالنصب عطف على قوله: هذا النوع، أي: أن تكون تلك المعرفة منسوبة إلى العلم نسبة الصفة إلى الموصوف.",
     "en": "In the accusative, coordinated with his words “this type” — that is: that that definiteness be related to the proper name with the relation of an attribute to that which it qualifies."},
]
