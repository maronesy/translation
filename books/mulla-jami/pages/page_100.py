# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 100 (printed ٩٩)."""

PAGE_NUMBER = 100
PRINTED_PAGE = "٩٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "الوصف[[١]] في سببية منع الصرف (أن يكون) وصفا (في الأصل[[٢]]) الذي هو الوضع بأن يكون وضعه على الوصفية،",
     "en": "The [requirement concerning the] adjective (al-waṣf), with respect to [its] being a cause of preventing full declension (manʿ al-ṣarf), is (that it be) an adjective (in the origin) — which is the [act of] coining (al-waḍʿ) — namely, that its coining be upon adjectivity;"},
    {"type": "matn",
     "ar": "لا أن تعرضه الوصفية بعد الوضع في الاستعمال، سواء بقي على الوصفية الأصلية أو زالت عنه.",
     "en": "not that adjectivity merely befalls it after the coining, in [the course of] usage — whether it has remained upon its original adjectivity or that [adjectivity] has departed from it."},
    {"type": "matn",
     "ar": "(فلا تضره[[٣]]) بأن تخرجه عن سببية منع الصرف (الغلبة) أي: غلبة الاسمية على الوصفية.",
     "en": "(So it is not harmed[[٣]]) — in the sense of being removed from [its] causing prevention of full declension — (by predominance, al-ghalaba); that is: the predominance of nounhood (al-ismiyya) over adjectivity."},
    {"type": "matn",
     "ar": "ومعنى الغلبة: اختصاصه ببعض أفراده، بحيث لا يحتاج في الدلالة عليه إلى قرينة،",
     "en": "The meaning of predominance is: its coming to be particular to some of its individual instances, such that no contextual indicator (qarīna) is needed to signify it,"},
    {"type": "matn",
     "ar": "كما أن «أسود» كان موضوعا لكل ما فيه سواد، ثم كثر استعماله في «الحية السوداء»، بحيث لا يحتاج في الفهم عنه إلى قرينة.",
     "en": "just as “aswad” (black) was coined for everything containing blackness, and then its use for “the black snake” (al-ḥayya al-sawdāʾ) became so frequent that no indicator is needed to understand it [in that sense]."},
    {"type": "matn",
     "ar": "(فلذلك[[٤]]) المذكور من اشتراط أصالة الوصفية وعدم مضرة الغلبة (صرف[[٥]]) لعدم أصالة الوصفية (أربع في) قولهم: «مررت بنسوة أربع»،",
     "en": "(So because of that[[٤]]) which has been mentioned — the stipulation of the originality of adjectivity and [the requirement of] the harmlessness of predominance — (“arbaʿ” was made fully declinable[[٥]]), on account of the non-originality of [its] adjectivity, (in) their saying: “I passed by four women (marartu bi-niswatin arbaʿin),”"},
    {"type": "matn",
     "ar": "(وامتنع) من الصرف، لعدم مضرة الغلبة (أسود[[٦]] وأرقم) حيث صارا اسمين (للحية) الأول: للحية السوداء، والثاني: للحية التي فيها سواد وبياض.",
     "en": "(and) — because the predominance is not harmful — (“aswad”[[٦]] and “arqam” were prevented) from full declension, they having become two nouns (for a snake): the first for the black snake, and the second for the snake in which there is black and white."},
    {"type": "matn",
     "ar": "(وأدهم) حيث صار اسما (للقيد) من الحديد، لما فيه من الدهمة، أعني: السواد،",
     "en": "(And “adham”) — it having become a noun (for the shackle, al-qayd) made of iron, because of the duhma (dark hue) in it, I mean: blackness —"},
    {"type": "matn",
     "ar": "فإن هذه الأسماء وإن خرجت عن الوصفية لغلبة الاسمية، لكنها بحسب أصل الوضع",
     "en": "for these nouns, even though they have departed from adjectivity owing to the predominance of nounhood, are nonetheless, in terms of the original coining,"},  # continues on the next page

    {"type": "rule"},

    # ---------------- Orphan continuation (tail of a footnote from p.99) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "الأصلي في «يعمل» بسبب عروض تاء تخرجه عن الوزن، فكيف يعتد بالوزن العارض مع كونه في الأصل خارجا عن شرط اعتبار الوزن.",
     "en": "…the original [pattern] in “yaʿmalu,” because of the accidental occurrence of a tāʾ that takes it out of the [verbal] pattern; so how can the accidental pattern (al-wazn al-ʿāriḍ) be given weight, when it is in origin outside the condition for reckoning the pattern?"},
    {"type": "pair",
     "ar": "قال السيد قدس سره: وليس أيضا بشيء ما قيل من أن المانع قبول تاء التأنيث، وهذه التاء ليست للتأنيث، بل للتذكير؛ لأن قولك: «أربعة رجال» أو «زيدين» باعتبار الجماعة، انتهى.",
     "en": "The Sayyid, may his secret be sanctified, said: Likewise there is no substance in what has been said — that the preventing factor is the admission of the feminine tāʾ — for this tāʾ is not for feminization but for masculinization; because your saying “arbaʿat rijāl” (four men), or “[four] Zayds,” is by consideration of the group [being male]. End [of quotation]."},
    {"type": "pair",
     "ar": "والتذكير مفهوم من اختصاصها بجماعة الذكور. ويؤيد ما قاله انقلاب التاء هاء في الوقف، وعدم انصراف قولهم: أربعة نصف ثمانية.",
     "en": "Masculinization is understood from its being restricted to a group of males. What he said is supported by the tāʾ's turning into a hāʾ in pause, and by the non-declension in their saying: “four is half of eight (arbaʿatun niṣfu thamāniya).”"},
    {"type": "pair",
     "ar": "وقال المصنف: التاء القادحة هي الداخلة قياسا، والتاء في أربعة ليست كذلك.",
     "en": "The author said: the impugning tāʾ (al-tāʾ al-qādiḥa) is the one that enters by analogy, whereas the tāʾ in “arbaʿa” is not of that kind."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ينبغي أن يقيد أيضا بألا يكون في العلم عند سيبويه، وألا يكون زائلا بالعلمية عند الأخفش.",
     "en": "It ought also to be qualified [by the requirement] that it not be [merely adjectival] within the proper name, according to Sībawayh; and that it not be one whose [adjectivity] has lapsed through proper-namehood (ʿalamiyya), according to al-Akhfash."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يجوز جعل «في الأصل» خبر «أن يكون»، فلا حاجة إلى تقدير وصفا حتى يتوهم جعل الاسم والخبر أمرا واحدا.",
     "en": "It is permissible to make “fī al-aṣl” (in the origin) the predicate of “an yakūna,” so there is no need to posit [an implied] “adjective” (waṣfan) — [a positing] that might give rise to the illusion of making the noun [of kāna] and the predicate one and the same thing."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الفاء للتفريع.",
     "en": "The fāʾ is for [drawing] a corollary (tafrīʿ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الفاء للنتيجة، فيدل على ترتيب العلم. واللام للتعليل، فيفيد ترتب المعلوم، فلا يغني أحدهما عن الآخر.",
     "en": "The fāʾ is for [indicating] the result (natīja), so it signals the ordering of the knowledge (tartīb al-ʿilm); and the lām is for causation (taʿlīl), so it conveys the ordering of the [thing] known (tarattub al-maʿlūm); thus neither of the two renders the other superfluous."},
    {"type": "pair",
     "ar": "وذلك إشارة إلى ما ذكر من مجموع الأصلين المترتب أحدهما على الآخر لا إلى الأصل الأول، ليصح عطف امتنع على صرف.",
     "en": "And “that” (dhālika) refers to what was mentioned of the totality of the two principles (al-aṣlayn), one of which is consequent upon the other — not to the first principle [alone] — so that the coordinating of “imtanaʿa” (it was prevented) upon “ṣurifa” (it was made declinable) may be valid."},
    {"type": "pair",
     "ar": "ووجه ذلك: أن يجعل مجموع المعطوف والمعطوف عليه متفرعا على مجموع الأصلين، ويحال رد كل فرع إلى أصله على ذهن المتعلم.",
     "en": "The manner of that is that the totality of the coordinated term and that upon which it is coordinated be made a corollary of the totality of the two principles, while the referring of each branch back to its own principle is left to the mind of the learner."},
    {"type": "pair",
     "ar": "وأما قوله: «وضعف» فهو عطف على صرف بلا إشكال.",
     "en": "As for his words “wa-ḍaʿufa” (and it was weakened), it is coordinated upon “ṣurifa” without any difficulty."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "نسب الصرف إلى الكل؛ لأنه صفة لجزئه.",
     "en": "He attributed the [full] declension to the whole [word], because it is an attribute of a part of it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: صرف «أسود» أو امتنع «أسود» من الصرف.",
     "en": "That is: “aswad” was made fully declinable, or “aswad” was prevented from full declension."},
]
