# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 375 (printed ٣٧٤)."""

PAGE_NUMBER = 375
PRINTED_PAGE = "٣٧٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإنها للإشارة إلى معانيها إشارة ذهنية لا حسية،» at the foot of PDF p. 374.
    {"type": "matn",
     "ar": "ومثل: «ذلكم الله ربكم»[[١]] مما ليس الإشارة إليه حسية محمول على التجوز[[٢]]،",
     "en": "…and such as “That is Allah, your Lord”, in which the pointing is not sensory, is taken as figurative usage (tajawwuz)."},
    {"type": "matn",
     "ar": "وإنما بنيت لشبهها بالحروف كما سبق.",
     "en": "They are indeclinable only because of their resemblance to particles, as has gone before."},
    {"type": "matn",
     "ar": "(وهي) أي: أسماء الإشارة («ذا»)[[٣]] حال كونها (للمذكر[[٤]]) الواحد، والعامل في الحال معنى الفعل المفهوم من نسبة الخبر إلى المبتدأ.",
     "en": "(They), that is, the demonstrative nouns, (are “dhā”) while it is (for the masculine) singular; the governor of the circumstantial accusative (ḥāl) is the verbal sense understood from the attribution of the predicate to the subject."},
    {"type": "matn",
     "ar": "(ولمثناه «ذان») رفعا (و«ذين») نصبا وجرا، أي: و«ذان وذين» حال كونهما لمثنى المذكر،",
     "en": "(For its dual, “dhāni”) in the nominative (and “dhayni”) in the accusative and genitive, that is, and “dhāni” and “dhayni” while they are for the masculine dual."},
    {"type": "matn",
     "ar": "قدم[[٥]] ليكون الضمير أقرب إلى مرجعه، وعلى هذا القياس في التراكيب الثلاثة الباقية،",
     "en": "He put [“li-muthannāhu”] first so that the pronoun would be nearer to its referent; the remaining three constructions follow the same pattern."},
    {"type": "matn",
     "ar": "فقوله: «هي» مبتدأ، وقوله: «ذا» مع ما عطف عليه مقيدا كل واحد منها بحال خبر له،",
     "en": "So his word “hiya” (they) is a subject, and his word “dhā”, together with what is conjoined to it, each of them restricted by a circumstantial qualifier, is its predicate."},
    {"type": "matn",
     "ar": "ويجيء في بعض اللغات «ذان» في جميع الأحوال الرفع والنصب والجر، ومنه قوله تعالى: «إن هذان لساحران»[[٦]] على أحد الوجوه[[٧]].",
     "en": "In some dialects “dhāni” occurs in all states — nominative, accusative and genitive — and of this is the word of the Exalted: “In hādhāni la-sāḥirāni” (These two are surely sorcerers), on one of the interpretations."},
    {"type": "matn",
     "ar": "(وللمؤنث) الواحدة («تا») قيل: هي الأصل في لغات المؤنث الواحدة؛ لأنها لم يثن منها إلا هي",
     "en": "(For the feminine) singular, (“tā”). It has been said that it is the original among the dialectal forms for the feminine singular, because no dual is formed from them except from it."},
    {"type": "matn",
     "ar": "(و«ذي») وقيل: هي الأصل، لكونها بإزاء «ذا» للمذكر، فينبغي أن يناسبها.",
     "en": "(And “dhī”). It has also been said that this is the original, because it stands opposite “dhā” for the masculine, so the one should correspond to the other."},
    {"type": "matn",
     "ar": "وقيل: هما أصلان، وللقول بأصالتهما قدمتا على سائرهما لفرعيتها (و«تي») بقلب",
     "en": "It has also been said that both are original; and because of the view that both are original, they were placed before the rest of them, which are derived. (And “tī”), by changing…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: as printed, ٦، ٦٢، ٦٤ follow «سورة فاطر» directly; «ذلكم الله ربكم» is at al-Zumar 39:6 and Ghāfir 40:62, 64; transcribed as printed.
    {"type": "pair",
     "ar": "سورة الأنعام: ١٠٢، سورة يونس: ٣، ٣٢، سورة فاطر: ١٣، ٦، ٦٢، ٦٤.",
     "en": "Qurʾān, Sūrat al-Anʿām 6:102; Sūrat Yūnus 10:3, 32; Sūrat Fāṭir 35:13, 6, 62, 64 [as printed; translator’s reference: the last three are al-Zumar 39:6 and Ghāfir 40:62, 64]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بتنزيله منزلة المحسوس المشاهد؛ إذ ما من شيء إلا ويدل عليه.",
     "en": "By treating it as something sensible and seen, since there is nothing that does not point to Him."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أن ذا ليس خبرا بل الخبر المجموع، فليس ذا فاعلا للنسبة حتى يصح جعله ذا حال، بل الفاعل هو المجموع من حيث المجموع، تدبر.",
     "en": "There is the point that “dhā” is not the predicate; the predicate is the whole. So “dhā” is not the agent of the attribution such that it could properly be made the possessor of the ḥāl (dhū al-ḥāl); the agent is the whole, as a whole. Reflect."},
    {"type": "pair",
     "ar": "ولولا هذه النقيضة لكان لتوجيهه الفضيلة. وقيل: خبر هي محذوف أي: هي خمسة.",
     "en": "Were it not for this defect, his interpretation would have the merit. It has been said: the predicate of “hiya” is omitted, that is, “they are five”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لما لم يصح حمل ذا على هي لعوده إلى الجمع احتاج إلى توجيه،",
     "en": "Since “dhā” cannot properly be predicated of “hiya”, as [hiya] refers to a plural, it needed an interpretation."},
    {"type": "pair",
     "ar": "فقال بعض المحشين: تارة بأن قوله: هي مبتدأ محذوف الخبر أي: وهي خمسة والجملة التي بعدها مبنية، والأولى أن يقال: وهي فيما سيذكر،",
     "en": "One of the glossators said: at one time, that his word “hiya” is a subject whose predicate is omitted, that is, “and they are five”, the sentence after it being explanatory; and it is better to say: “and they are in what will be mentioned”;"},
    # REVIEW: «وهى» printed (final yāʾ without dots), elsewhere in this note «وهي»; transcribed as printed.
    {"type": "pair",
     "ar": "وتارة بأن ذا خبر بتقدير معطوف أي: وهى ذا وأخواته. وقوله: للمذكر خبر مبتدأ محذوف أي: هو للمذكر.",
     "en": "and at another time, that “dhā” is the predicate with a conjoined noun understood, that is, “and they are dhā and its sisters”. His word “li-l-mudhakkar” (for the masculine) is the predicate of an omitted subject, that is, “it is for the masculine”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يمكن أن يقال: إنه قدم؛ لأن الذهن ينساق إلى ذكر المثنى والجمع بعد ذكر المفرد.",
     "en": "It may be said that he put it first because the mind moves on to the mention of the dual and the plural after the mention of the singular."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة طه: ٦٣.",
     "en": "Qurʾān, Sūrat Ṭā Hā 20:63."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ثانيها: أن ههنا بمعنى نعم. وثالثها: ضمير الشأن محذوف هكذا نقل عنه في الحاشية.",
     "en": "The second of them: that “in” here means “naʿam” (yes). The third: that the pronoun of the matter is omitted. This is how it is reported from him in the gloss."},
    {"type": "pair",
     "ar": "ويرد الوجه الثاني أن لام الابتداء لا يدخل على خبر المبتدأ. والثالث: أن حذف ضمير الشأن ضعيف.",
     "en": "Against the second interpretation stands [the objection] that the lām of inception (lām al-ibtidāʾ) does not enter upon the predicate of a subject; and against the third, that omitting the pronoun of the matter is weak."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قال قدس سره في الحاشية: وقيل: إن ههنا بمعنى نعم، وهذان مبتدأ، ولساحران خبره.",
     "en": "ʿAbd al-Ghafūr said: He — may his secret be sanctified — said in the gloss: it has been said that “in” here means “naʿam”, “hādhāni” is a subject, and “la-sāḥirāni” its predicate."},
    {"type": "pair",
     "ar": "وقيل: ضمير الشأن ههنا محذوف أي: إنه هذان لساحران.",
     "en": "It has also been said that the pronoun of the matter is omitted here, that is, “innahu hādhāni la-sāḥirāni” (indeed, it is [that] these two are surely sorcerers)."},
]
