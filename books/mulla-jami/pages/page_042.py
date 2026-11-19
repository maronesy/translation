# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 42 (printed ٤١)."""

PAGE_NUMBER = 42
PRINTED_PAGE = "٤١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "على معنى مفرد بالوضع»، فمثل: «عبد الله» علما خرج عنه، فإنه لا يقال له: «لفظة واحدة»[[١]].",
     "en": "…upon a single meaning by way of positing (waḍʿ)” — then the like of “ʿAbd Allāh” as a proper name is excluded by it [this definition], for it is not said of it that it is “a single utterance (lafẓa wāḥida).”"},
    {"type": "matn",
     "ar": "وبقي مثل: «الرجل»، و«قائمة»، و«بصري»[[٢]] مما يعد لشدة الامتزاج لفظة واحدة داخلا فيه، فأخرجه بقيد الإفراد، ولو لم يخرجه بتركه لكان أنسب[[٣]]، كما عرفت.",
     "en": "But the like of “al-rajul,” “qāʾima,” and “baṣrī” — which is counted, on account of intensity of fusion, as a single utterance — remained included within it, so he excluded it by the restriction of singularity (ifrād); yet had he not excluded it, by dropping [that restriction], it would have been more fitting, as you have come to know."},
    {"type": "matn",
     "ar": "واعلم أن الوضع يستلزم الدلالة؛ لأن الدلالة: كون الشيء بحيث يفهم منه شيء آخر، فمتى تحقق الوضع تحققت الدلالة.",
     "en": "Know that positing (waḍʿ) necessarily entails signification (dalāla), because signification is: a thing’s being such that something else is understood from it; so whenever positing is realized, signification is realized."},
    {"type": "matn",
     "ar": "فبعد ذكر الوضع لا حاجة إلى ذكر الدلالة،",
     "en": "Hence, after mentioning positing, there is no need to mention signification;"},
    {"type": "matn",
     "ar": "لكن الدلالة لا تستلزم الوضع لإمكان أن تكون بالعقل، كدلالة لفظ «ديز» المسموع من وراء الجدار على وجود اللافظ،",
     "en": "but signification does not necessarily entail positing, since it may be by reason (ʿaql) — like the signification of the utterance “dīz,” heard from behind a wall, pointing to the existence of an utterer —"},
    {"type": "matn",
     "ar": "وأن تكون بالطبع، كدلالة لفظ «أح أح» على وجع الصدر، فبعد ذكر الدلالة لا بد من ذكر الوضع، كما في المفصل.",
     "en": "and it may be by nature (ṭabʿ) — like the signification of the utterance “aḥ aḥ” pointing to chest pain; so after mentioning signification it is indispensable to mention positing, as in al-Mufaṣṣal."},

    {"type": "section", "ar": "[أقسام الكلمة]",
     "en": "The Divisions of the Word (kalima)"},

    {"type": "matn",
     "ar": "(وهي)[[٤]] أي: الكلمة (اسم، وفعل، وحرف)[[٥]] أي: منقسمة إلى هذه الأقسام الثلاثة منحصرة فيها[[٦]]،",
     "en": "(And it) — that is, the word (kalima) — (is a noun (ism), a verb (fiʿl), and a particle (ḥarf)) — that is, it is divided into these three divisions and confined to them,"},
    {"type": "matn",
     "ar": "(لأنها)[[٧]] أي: الكلمة لما كانت موضوعة لمعنى، والوضع",
     "en": "(because it) — that is, the word — since it was posited for a meaning, and positing…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هكذا قالوه. وفيه أنه إن أريد باللفظة أدنى ما يطلق عليه اللفظ كهمزة الاستفهام لم يدخل في التعريف إلا نزر من الكلمات.",
     "en": "Thus they stated it. But there is [an objection] in it: if by “the utterance (lafẓa)” is meant the least of that to which “utterance” is applied — like the interrogative hamza — then only a scant few of the words would fall under the definition."},
    {"type": "pair",
     "ar": "وإن أريد ما له نوع وحدة لم يخرج منه مثل «عبد الله» علما. وإن أريد خصوص وحدة فلا يدل اللفظة عليه.",
     "en": "And if what is meant is that which possesses some kind of unity, then the like of “ʿAbd Allāh” as a proper name is not excluded from it; and if a specific unity is meant, then the utterance (lafẓa) does not signify it."},
    {"type": "pair",
     "ar": "إن قلت: اللفظة للمرة، والمفهوم منها ما تكلم به دفعة؟",
     "en": "If you say: “the utterance (lafẓa)” denotes a single instance (marra), and what is understood from it is what is uttered at one go (dufʿatan)?"},
    {"type": "pair",
     "ar": "قلنا: لا شبهة في جواز التكلم بـ«عبد الله» علما به كذلك، بل يجب أن يتكلم به دفعة،",
     "en": "We say: there is no doubt as to the permissibility of uttering “ʿAbd Allāh” as a proper name in that manner [at one go]; rather, it must be uttered at one go,"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: المراد بالمرة ما تكلم به مرة، وليس ما يصح فيه أن يتكلم به مرتين.",
     "en": "unless it be said: what is meant by “a single instance” is that which is uttered once, and not that which it is valid to utter twice."},
    {"type": "pair",
     "ar": "فخرج عنه «عبد الله» علما لاشتماله على كلمتين يصح أن يتكلم بهما مرتين.",
     "en": "So “ʿAbd Allāh” as a proper name is excluded from it, because it comprises two words which may validly be uttered twice."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: قبل ملاحظة قيد الإفراد، أو المراد أنه بقي في قيد إخراج ذلك القيد مثل: «عبد الله».",
     "en": "That is: before taking the restriction of singularity (ifrād) into account; or what is meant is that it remained [caught] within the restriction — [namely] that restriction’s excluding the like of “ʿAbd Allāh.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولك أن تقول: المراد بالمفرد أعم من المفرد حقيقة أو حكما.",
     "en": "You may say: what is meant by “the single (mufrad)” is more general than the singular in reality (ḥaqīqatan) or [the singular] in ruling (ḥukman)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا يقال: الضمير إما أن يرجع إلى لفظ الكلمة، أو إلى مفهومها، وعلى التقديرين لا يصح الحكم عليها بأنها اسم وفعل وحرف؛",
     "en": "It should not be objected: the pronoun [in “and it”] either refers back to the wording “al-kalima” or to its concept (mafhūm); and on either assumption it is not valid to predicate of it that it is “a noun, a verb, and a particle”;"},
    {"type": "pair",
     "ar": "لأنا نقول: المراد مفهومه، والمعنى أن هذا المفهوم منقسم إلى هذه الأقسام.",
     "en": "because we say: what is meant is its concept (mafhūm); and the meaning is that this concept is divided into these divisions."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "السر في تثليث القسمة تباين أحوال الأقسام واختلافها مادة وصورة للكلام.",
     "en": "The secret behind making the division threefold is the disparity of the states of the divisions and their difference, in matter and in form, with respect to speech (kalām)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لما كان الغالب في التقسيم قصد الحصر فيما يذكر من الأقسام، وقد يخلو عنه أيضا، صرح بأن المراد ههنا الحصر.",
     "en": "Since the intent of exhaustive restriction (ḥaṣr) predominates in what is mentioned of the divisions — though [a division] may also be devoid of it — he stated explicitly that what is intended here is restriction."},
    {"type": "pair",
     "ar": "وإرادة الحصر إما مفهوم من قوله: «لأنها إما أن تدل» إلى آخره، أو من السكوت في معرض بيان الأقسام.",
     "en": "And the intending of restriction is either understood from his words “because they either signify…” to the end [of the passage], or from [his] silence in the context of expounding the divisions."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "متعلق بما يفهم من الجملة السابقة من معنى الانقسام أو الانحصار.",
     "en": "It is connected to what is understood from the preceding sentence of the sense of division or restriction."},
    {"type": "pair",
     "ar": "ويكفي هذا القدر للظرف عند بعض النحاة من غير اعتبار لفظ في نظم الكلام، على ما قالوا: إن الظرف يكفيه رائحة الفعل. وبعضهم…",
     "en": "This much suffices for the adverbial/prepositional phrase (ẓarf) according to some grammarians, without regard to an [explicit] word in the construction of the speech — as they have said: “the ẓarf is satisfied with [merely] a whiff (rāʾiḥa) of the verb.” And some of them…"},
]
