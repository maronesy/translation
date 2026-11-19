# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 372 (printed ٣٧١)."""

PAGE_NUMBER = 372
PRINTED_PAGE = "٣٧١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وإلا فالعرب لا يعرف المبتدأ والخبر» at the foot of PDF p. 371; here the matn resumes with the next lemma.
    {"type": "matn",
     "ar": "(وما بعده خبره) فقوله: «خبره» إما مرفوع على أنه خبر، والجملة حال، أو منصوب عطفا على ثاني مفعولي «يجعله»،",
     "en": "(and what follows it its predicate). His word “khabarahu / khabaruhu” (its predicate) is either nominative, as a predicate, the sentence being a circumstantial clause (ḥāl), or accusative, conjoined to the second of the two objects of “yajʿaluhu” (makes it)."},
    {"type": "matn",
     "ar": "وإنما يعرف من العرب جعله مبتدأ برفع ما بعده في مثل: «كنت أنت الرقيب»[[١]]، و«علمت زيدا هو المنطلق»،",
     "en": "Their making it a subject is known from the Arabs only through their putting what follows it in the nominative, in such as “kunta anta al-raqību” (You were the Watcher) and “ʿalimtu Zaydan huwa al-munṭaliqu” (I knew Zayd — he is the one departing)."},
    {"type": "matn",
     "ar": "وفي بعض نسخ المتن: «مبتدأ ما بعده خبره» بدون الواو، وحينئذ الرفع متعين.",
     "en": "In some copies of the matn [it reads]: “a subject, what follows it its predicate”, without the wāw; in that case the nominative is the only option."},
    {"type": "matn",
     "ar": "(ويتقدم قبل الجملة[[٢]]) وإيراد لفظ «قبل» لتأكيد التقدم؛ لأن تقدم الضمير على مرجعه غير معهود،",
     "en": "(It precedes, before the sentence). The word “qabla” (before) is brought in to emphasize the precedence, because a pronoun’s preceding its referent is not customary."},
    {"type": "matn",
     "ar": "ولا يبعد أن يقال معنى الكلام: ويقع متقدما من غير سبق مرجع، وذلك بحسب المفهوم أعم من أن يكون قبل الجملة أو لا،",
     "en": "It is not far-fetched to say that the meaning of the statement is: it occurs in front, without a referent having gone before; and that, in terms of its concept, is more general than its being before the sentence or not;"},
    {"type": "matn",
     "ar": "فلذلك قيده بقوله: «قبل الجملة» أي: قبل هذا الجنس من الكلام[[٣]]",
     "en": "therefore he restricted it with his words “before the sentence”, that is, before this genus of speech:"},
    {"type": "matn",
     "ar": "(ضمير غائب[[٤]] يسمى «ضمير الشأن») إذا كان مذكرا رعاية للمطابقة، لا أن الضمير راجع إليه",
     "en": "(a third-person pronoun, called “the pronoun of the matter”) (ḍamīr al-shaʾn) when it is masculine, out of regard for agreement — not that the pronoun refers back to it —"},
    {"type": "matn",
     "ar": "(و) ضمير (القصة) إذا كان مؤنثا، ويحسن تأنيثه[[٥]] إذا كان العمدة فيها مؤنثا[[٦]] ليحصل المناسبة",
     "en": "(and) the pronoun (of the story) (ḍamīr al-qiṣṣa) when it is feminine. Making it feminine is good when the principal element (ʿumda) in it is feminine, so that correspondence obtains."},
    {"type": "matn",
     "ar": "(يفسر) ذلك الضمير الغائب لإبهامه (بالجملة) المذكورة (بعده) أي: بهذه الحصة من الجنس المذكور.",
     "en": "(It is explained) — that third-person pronoun, because of its vagueness — (by the sentence) mentioned (after it), that is, by this portion of the genus mentioned."},
    {"type": "matn",
     "ar": "والظاهر أن قوله: «يسمى ضمير الشأن والقصة» جملة معترضة، بيان للواقع ليس داخلا في بيان القاعدة،",
     "en": "What is apparent is that his words “called the pronoun of the matter and of the story” are a parenthetical clause, a statement of fact that does not enter into the statement of the rule,"},
    {"type": "matn",
     "ar": "فإنه لا دخل للتسمية في هذا الحكم، فإنه ثابت سواء وقع هذه التسمية أو لا،",
     "en": "for the naming has no bearing on this ruling, since the ruling holds whether this naming occurs or not."},
    {"type": "matn",
     "ar": "وأيضا يلزم استدراك قوله[[٧]]: «يفسر بالجملة بعده»، فعلى هذا لو لم",
     "en": "Further, [otherwise] his words “explained by the sentence after it” would be redundant. On this [view], if…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة المائدة: ١١٧.",
     "en": "Qurʾān, Sūrat al-Māʾida 5:117."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "تلك الجملة الخبرية اسمية البتة إلا إذا دخلت عليه نواسخ المبتدأ، فإنه حينئذ يجوز أن تكون فعلية",
     "en": "That predicative sentence is always nominal, except when the abrogators of the subject (nawāsikh al-mubtadaʾ) enter upon it; for then it may be verbal,"},
    {"type": "pair",
     "ar": "كقوله تعالى: «فإنها لا تعمى الأبصار» (الحج:٤٦).",
     "en": "as in the words of the Exalted: “For indeed it is not the eyes that are blind” (Qurʾān, Sūrat al-Ḥajj 22:46)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جعل الجملة للجنس ليجعل الجملة بعده حصة منه فيتغايران ردا على من قال: وضع الظاهر موضع المضمر؛",
     "en": "He took “the sentence” as generic so as to make the sentence after it a portion of it, so that the two differ — in reply to one who said: [then] an explicit noun has been put in the place of a pronoun;"},
    {"type": "pair",
     "ar": "لأن تفسير الضمير بالجملة خلاف ما هو شأنه فكان من مظان التقرير.",
     "en": "because explaining a pronoun by a sentence is contrary to what is its normal way, so it was a place calling for firm establishment."},
    {"type": "pair",
     "ar": "ولا يخفى أن ما قيل أهون مما ارتكبه، فتدبر أحسن التدبر واختر.",
     "en": "It is not hidden that what was said is less grave than what he resorted to; so reflect with the best reflection, and choose."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن المراد به الشأن والقصة، وهو مفرد غائب، فيلزمه الإفراد والغيبة",
     "en": "Because what is meant by it is the matter or the story, and that is a singular third-person [referent], so singular and third person are necessary to it,"},
    {"type": "pair",
     "ar": "بخلاف صيغة الفصل، فإنها عبارة عن المبتدأ، فيلزم مطابقتها له كما ذكر.",
     "en": "unlike the form of the separator (faṣl), for it denotes the subject, so it must agree with it, as was mentioned."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: تأنيث هذا الضمير، وإن لم يتضمن الجملة المفسرة مؤنثا قياس؛ لأن ذلك باعتبار القصة، لكن لم يسمع.",
     "en": "Shaykh al-Raḍī said: making this pronoun feminine, even when the explaining sentence contains no feminine, is analogically valid (qiyās), because that is with respect to “the story”; but it is not attested."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وجه حسنه أنه المسموع.",
     "en": "The reason it is good is that it is what is attested."},
    {"type": "pair",
     "ar": "وأما تأنيثه بتأويله بالقصة من غير كون العمدة فيها مؤنثا، فمجرد قياس حال عن السماع، كما حققه الرضي.",
     "en": "As for making it feminine by interpreting it as “the story” without the principal element in it being feminine, that is mere analogy devoid of attestation, as al-Raḍī established."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فيه بحث؛ لأنه قاعدة أخرى مبنية لوجوب تفسيره بهذه الجملة دون أمر آخر من تمييز أو حرف تفسير.",
     "en": "This is open to question, because it is another rule, set out to state that it must be explained by this sentence and not by something else, such as a specifying accusative (tamyīz) or a particle of explanation."},
    {"type": "pair",
     "ar": "اعلم أنه يجوز ذكر الضمير من غير سبق مرجع إذا تعين المرجع من غير حاجة إلى مفسر،",
     "en": "Know that a pronoun may be mentioned without a referent going before it when the referent is determinate without need of an explainer;"},
    {"type": "pair",
     "ar": "ويصح أن يكون ضمير الشأن منه باعتبار أنه راجع إلى الشأن والقصة لتعينه في المقام، فيكون ما بعده خبرا صرفا",
     "en": "and the pronoun of the matter may properly be of this kind, in that it refers to the matter or the story because that is determinate in the context, so that what follows it is purely a predicate…"},
]
