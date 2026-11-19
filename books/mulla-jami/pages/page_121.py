# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 121 (printed ١٢٠)."""

PAGE_NUMBER = 121
PRINTED_PAGE = "١٢٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(إذا نكر) بأن يؤول العلم بواحد من الجماعة[[١]] المسماة به[[٢]]، نحو: «هذا زيد، ورأيت زيدا آخر»، فإنه أريد به المسمى بزيد،",
     "en": "(When it is made indefinite): namely, that the proper name be construed [figuratively] as “one of the group named by it,” as in “this is a Zayd, and I saw another Zayd,” for what is meant by it is “the one named Zayd”;"},
    {"type": "matn",
     "ar": "أو يجعل عبارة عن الوصف المشتهر صاحبه[[٣]] به، نحو قولهم: «لكل فرعون موسى»، أي: لكل مبطل محق",
     "en": "or it is made an expression for the attribute by which its bearer is renowned, as in their saying “to every Pharaoh a Moses,” that is: for every falsifier a vindicator of truth;"},
    {"type": "matn",
     "ar": "(صرف لما تبين) أي: ظهر حين بين[[٤]] أسباب منع الصرف وشرائطها فيما سبق (من أنها) أي: العلمية (لا تجامع مؤثرة إلا ما) أي: السبب الذي (هي) أي: العلمية (شرط فيه)",
     "en": "(it is fully inflected, because of what has become clear) — that is, what became evident when he expounded the causes of denying full inflection and their conditions in what preceded — (namely, that it) — i.e., proper-nounhood — (does not coincide, as operative, except with that which) — i.e., the cause of which — (it) — i.e., proper-nounhood — (is a condition therein)."},
    {"type": "matn",
     "ar": "وذلك في التأنيث بالتاء لفظا أو معنى، والعجمة، والتركيب، والألف والنون المزيدتين، فإن كل واحدة من هذه الأسباب الأربعة مشروطة بالعلمية",
     "en": "That is [the case] with feminineness by the tāʾ — in wording or in meaning — with non-Arabic origin (ʿujma), with compounding (tarkīb), and with the augmented alif and nūn; for each one of these four causes is conditioned by proper-nounhood."},
    {"type": "matn",
     "ar": "(إلا العدل ووزن الفعل) استثناء مما بقي من الاستثناء الأول[[٥]]، أي: لا تجامع غير ما هي شرط فيه، إلا العدل ووزن الفعل،",
     "en": "(except deviation and the verbal pattern): an exception from what remains after the first exception — that is, [proper-nounhood] does not coincide with anything other than that in which it is a condition, save deviation (al-ʿadl) and the verbal pattern (wazn al-fiʿl),"},
    {"type": "matn",
     "ar": "فإن العلمية تجامعهما مؤثرة، كما في «عمر» و«أحمد»[[٦]]، وليست شرطا فيهما،",
     "en": "for proper-nounhood does coincide with these two as operative, as in “ʿUmar” and “Aḥmad,” and it is not a condition in them,"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: بمفهوم صالح لأن يراد به واحد من الجماعة.",
     "en": "That is: by a concept fit for “one of the group” to be meant by it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "المراد بالجماعة: ما فوق الواحد. فلا يرد أنه يوجب ألا ينكر المشترك بين اثنين.",
     "en": "What is meant by “the group” is more than one. So it is no objection [to say] that this would entail that what is shared between [only] two could not be made indefinite."},
    {"type": "pair",
     "ar": "والمعنى يؤول بمفهوم المسمى المنكر، فيكون معنى هذا زيد، هذا مسمى بزيد.",
     "en": "The sense is construed by the concept of the indefinite “the named one,” so that the meaning of “this is a Zayd” is “this is one named Zayd.”"},
    {"type": "pair",
     "ar": "فقوله: واحد من الجماعة المسماة به بمعنى مسمى به، فلا حاجة إلى تأويله بمفهوم صادق على واحد من الجماعة، كما ظن به بعض الظن.",
     "en": "So his phrase “one of the group named by it” means “one named by it,” and there is no need to construe it by a concept true of one of the group, as some have supposed [it to be]."},
    {"type": "pair",
     "ar": "وقوله: «فإنه أريد به المسمى» أي: هذا المفهوم في ضمن فرد ما، فاللام فيه للعهد الذهني، وكان الأوضح أن يقول: مسمى بزيد،",
     "en": "And his phrase “for what is meant by it is ‘the named one’” means: this concept as [embedded] within some particular instance; so the definite article in it is for mental determination (al-ʿahd al-dhihnī); and it would have been clearer for him to say “named Zayd.”"},
    {"type": "pair",
     "ar": "ومما يجب أن ينبه عليه في هذا المقام، ولم يتنبه له أحد أن المراد بالتنكير التنكير حكما؛ إذ بالتأويل لا يصير نكرة حقيقية؛ إذ النكرة الحقيقية ما وضع لغير معين، لا ما أريد به غير معين مجازا.",
     "en": "And among the things that must be pointed out in this context — which no one has noticed — is that what is meant by “indefiniteness” is indefiniteness in ruling (ḥukman); for by [mere figurative] construal it does not become a true indefinite, since the true indefinite is what is coined for a non-specific referent, not what has a non-specific referent intended by it figuratively (majāzan)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيد الاشتهار باعتبار الأغلب، وإلا يجوز أن يؤول بوصف غير مشتهر بقرينة.",
     "en": "The restriction “renowned” is by consideration of what is predominant; otherwise it is permissible for it to be construed by an attribute that is not renowned, [when established] by a contextual indicator (qarīna)."},
    {"type": "pair",
     "ar": "واعلم أن العلم الذي كان في الأصل وصفا، واشتهر مسماه بهذه الصفة الأصلية، فإذا نكر بإرادة هذه الصفة لا شك أنه يعود فيه الوصفية، فلا يلزم بهذا النوع من التنكير أن يكون منصرفا، فتأمل.",
     "en": "Know that a proper name which was originally an attribute, and whose bearer became renowned by this original attribute — when it is made indefinite by intending this attribute, there is no doubt that descriptiveness returns to it, so it does not follow that by this kind of indefiniteness it must be fully inflected; so ponder it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: ظهر من غير بيانه، بل في ضمن بيان أسباب منع الصرف وشرائطها. ولذا اختار «تبين» على «بين».",
     "en": "He means: it became evident without his [expressly] declaring it, but rather within [his] exposition of the causes of denying full inflection and their conditions. For this reason he chose “tabayyana” (became clear) over “bayyana” (he declared)."},
    {"type": "pair",
     "ar": "ولا يخفى عليك أن كلام المصنف مغلق. ولو قال: كل ما فيه علمية مؤثرة إذا نكر صرف؛ لأنه إذا نكر بقي بلا سبب أو على سبب واحد لما تبين إلى آخره لكان واضحا.",
     "en": "It is not hidden from you that the author’s wording is obscure. Had he said: “everything in which there is operative proper-nounhood, when made indefinite, is fully inflected, because when made indefinite it remains with no cause, or upon a single cause, in accordance with what has become clear,” and so forth — it would have been plain."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: استثناء بعد تقييد المستثنى منه بالاستثناء الأول، فلم يلزم تعدد الاستثناء من أمر واحد بلا عاطف؛ لأن الأول استثناء من المطلق، والثاني استثناء من المقيد.",
     "en": "That is: an exception after the qualification of the thing excepted from by the first exception, so that no multiplicity of exceptions from a single matter without a conjunction is entailed; for the first is an exception from the unqualified, and the second an exception from the qualified."},
    {"type": "pair",
     "ar": "ونظير ذلك ما يقال في توجيه ظرفين من جنس: إذا كانا متعلقين بفعل واحد بلا عاطف.",
     "en": "The parallel of this is what is said in accounting for two adverbials of one kind when they are both governed by a single verb without a conjunction."},
    {"type": "pair",
     "ar": "ولو جعل المصنف قوله: «العدل ووزن الفعل» معطوفا على قوله: «ما هي شرط فيه» لكان أظهر دلالة، وأخصر عبارة.",
     "en": "Had the author made his phrase “deviation and the verbal pattern” conjoined to his phrase “that in which it is a condition,” it would have been more evident in signification and more concise in expression."},
    {"type": "pair",
     "ar": "ولعل النكتة في الفصل اختلاف تأثير العلمية في المعطوف والمعطوف عليه وغرابة الأسلوب.",
     "en": "Perhaps the subtle point in [his] separating [them] is the difference in the effect of proper-nounhood upon the conjoined and that to which it is conjoined, and [a striving for] a striking mode of expression."},

    # ---------------- Footnote 6 (continues on the next page) ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "اتفق النحاة على أن العلمية مؤثرة مع العدل في اسم لم يوضع إلا علما كعمر، ومع وزن الفعل سواء كان الاسم غير منصرف قبل العلمية كأحمد أو لا كأصبع ويزيد.",
     "en": "The grammarians agreed that proper-nounhood is operative — together with deviation — in a noun that was coined only as a proper name, such as “ʿUmar,” and together with the verbal pattern, whether the noun was imperfectly inflected before proper-nounhood, like “Aḥmad,” or not, like “Iṣbaʿ” and “Yazīd.”"},
    {"type": "pair",
     "ar": "واختلفوا في تأثيرها مع العدل في اسم كان غير منصرف قبل العلمية كثلاث ومثلث. فذهب أكثر النحاة إلى انصرافه؛ لأن العدل تابع",
     "en": "They differed regarding its effect, together with deviation, in a noun that was imperfectly inflected before proper-nounhood, such as “thulāth” and “mathlath.” Most grammarians held that it is fully inflected, because deviation is subordinate…"},
]
