# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 296 (printed ٢٩٥)."""

PAGE_NUMBER = 296
PRINTED_PAGE = "٢٩٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows the first of the five readings at the foot of PDF p. 295 (new sentence).
    {"type": "matn",
     "ar": "(و) الثاني: (فتح الأول ونصب الثاني) أي: «لا حول ولا قوة إلا بالله».",
     "en": "(And) the second: (the fatḥa on the first and the accusative on the second), that is, “lā ḥawla wa-lā quwwatan illā bi-llāh.”"},
    {"type": "matn",
     "ar": "أما فتح الأول: فلأن «لا» الأولى لنفي الجنس.",
     "en": "As for the fatḥa on the first, it is because the first “lā” negates the genus."},
    {"type": "matn",
     "ar": "وأما نصب الثاني: فلأن «لا» الثانية مزيدة[[١]] لتأكيد النفي والثاني معطوف[[٢]] على الأول، فيكون منصوبا حملا على لفظه لمشابهة حركته حركة الإعراب[[٣]]،",
     "en": "As for the accusative on the second, it is because the second “lā” is added to reinforce the negation, and the second [noun] is conjoined to the first, so it is accusative by construction on its form (ḥamlan ʿalā lafẓihi), since its vowel resembles a vowel of inflection."},
    {"type": "matn",
     "ar": "ويجوز أن يقدر لهما[[٤]] خبر واحد، وأن يقدر لكل منهما خبر على حدة.",
     "en": "One may suppose a single predicate for the two, or suppose a separate predicate for each of them."},
    {"type": "matn",
     "ar": "(و) الثالث: (فتح الأول ورفع الثاني) نحو: «لا حول ولا قوة إلا بالله».",
     "en": "(And) the third: (the fatḥa on the first and the nominative on the second), as in “lā ḥawla wa-lā quwwatun illā bi-llāh.”"},
    {"type": "matn",
     "ar": "أما فتح الأول: فلأن «لا» الأولى لنفي الجنس.",
     "en": "As for the fatḥa on the first, it is because the first “lā” negates the genus."},
    {"type": "matn",
     "ar": "وأما رفع الثاني: فلأن «لا» زائدة والثاني معطوف على محل الأولى؛ لأنه مرفوع بالابتداء",
     "en": "As for the nominative on the second, it is because the “lā” is redundant and the second is conjoined to the position (maḥall) of the first, since that is in the nominative as a subject of a nominal sentence;"},
    {"type": "matn",
     "ar": "عطف مفرد على مفرد بأن يقدر لهما خبر واحد، أو عطف جملة على جملة بأن يقدر لكل منهما خبر واحد.",
     "en": "[it is] the conjunction of a single term to a single term, by supposing one predicate for the two, or the conjunction of a sentence to a sentence, by supposing a predicate for each of them."},
    {"type": "matn",
     "ar": "(و) الرابع: (رفعهما) بالابتداء، نحو: «لا حول ولا قوة إلا بالله»؛",
     "en": "(And) the fourth: (the nominative on both), as subjects, as in “lā ḥawlun wa-lā quwwatun illā bi-llāh,”"},
    {"type": "matn",
     "ar": "لأنه جواب قولهم: «أبغير الله حول وقوة؟»، فجاء بالرفع فيهما مطابقة للسؤال،",
     "en": "because it answers their saying, “Is there power and strength through other than Allah?”; so the nominative came in both in correspondence with the question."},
    {"type": "matn",
     "ar": "ويجوز الأمران ههنا أيضا.",
     "en": "Both [analyses] are permitted here too."},
    {"type": "matn",
     "ar": "(و) الخامس: (رفع الأول) على أن «لا» بمعنى «ليس» (على ضعف) فإن عمل «لا» بمعنى «ليس» قليل",
     "en": "(And) the fifth: (the nominative on the first), with “lā” in the sense of “laysa,” (weakly), for the government of “lā” in the sense of “laysa” is rare,"},
    {"type": "matn",
     "ar": "(وفتح الثاني) نحو: «لا حول ولا قوة إلا بالله» على أن يكون «لا» لنفي الجنس،",
     "en": "(and the fatḥa on the second), as in “lā ḥawlun wa-lā quwwata illā bi-llāh,” with the [second] “lā” negating the genus."},
    {"type": "matn",
     "ar": "وضعف[[٥]] وجه ضعف رفع الأول بأنه يجوز أن يكون رفعه لإلغاء عمل «لا» بالتكرير لا لكونها بمعنى «ليس»[[٦]]؛",
     "en": "The account of the weakness of the nominative on the first has been judged weak, on the ground that its nominative may be due to the cancellation of the government of “lā” through repetition, not to its being in the sense of “laysa”;"},
    {"type": "matn",
     "ar": "لأن شرط صحة إلغائها التكرير فقط، وقد حصل ههنا، ولا دخل فيها، لتوافق الاسمين بعدها في الإعراب، فهذا على",
     "en": "for the condition for the soundness of its cancellation is repetition alone, and that is present here; and the agreement of the two nouns after it in inflection has no bearing on it. So this is on…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: يجوز أن يجعل «لا» غير زائدة، بل لنفي الجنس، لكن تلغيها عن العمل",
     "en": "Shaykh al-Raḍī said: one may make the “lā” not redundant but negating the genus, while cancelling its government,"},
    {"type": "pair",
     "ar": "لجواز إلغائها إذا كان اسمها نكرة غير مفصولة بشرط التكرير سواء ألغيت الأولى أو الثانية أو كلتاهما.",
     "en": "since its cancellation is permitted when its noun is indefinite and not separated, on condition of repetition, whether the first, the second, or both are cancelled."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: «مضي الخبر» is clearly printed but its sense here is unclear; transcribed as printed.
    {"type": "pair",
     "ar": "على محل الأول. والقياس في ذلك مضي الخبر كما في «إن».",
     "en": "[Conjoined] to the position of the first. The analogical rule in this is the predicate’s “passing” (muḍiyy al-khabar), as with “inna.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أو حملا على محله القريب، فإن الاسم لا محلين قريب وهو النصب، وبعيد وهو الرفع بالابتداء.",
     "en": "Or by construction on its near position; for the noun of lā has two positions: a near one, which is the accusative, and a far one, which is the nominative as subject."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «خبر واحد وعند سيبويه», yet the next sentence says one predicate is not allowed by Sībawayh; the sense suggests «عند غير سيبويه»; transcribed as printed.
    {"type": "pair",
     "ar": "خبر واحد وعند سيبويه، فإن «لا» عاملة عند غيره في المتبوع والتابع.",
     "en": "A single predicate, and according to Sībawayh; for according to others “lā” governs both the antecedent (matbūʿ) and the dependent (tābiʿ)."},
    {"type": "pair",
     "ar": "وأما عند سيبويه، فلا يجوز تقدير خبر واحد؛ لأن «لا» عنده مع اسمه المبني مبتدأ، والمعطوف منصوب بـ«لا»،",
     "en": "According to Sībawayh, however, supposing a single predicate is not permitted, because in his view “lā” together with its indeclinable noun is a subject (mubtadaʾ), while the conjoined noun is put in the accusative by “lā”;"},
    {"type": "pair",
     "ar": "فيرتفع الخبر بعاملين مختلفين، فيجب أن يقدر لكل منهما خبر.",
     "en": "so the predicate would be made nominative by two different governors; hence a predicate must be supposed for each of them."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "المضعف الشيخ الرضي.",
     "en": "The one who judged it weak is Shaykh al-Raḍī."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ لم يثبت في كلامهم عمل «لا» عمل «ليس»، بل لم يره إلا كون اسم بعدها مرفوعا والخبر محذوفا نحو: لا براح ولا مستصرخ،",
     "en": "Since the government of “lā” in the manner of “laysa” is not established in their speech; rather, he saw nothing but a noun after it in the nominative with the predicate elided, as in “lā barāḥun” (there is no leaving) and “wa-lā mustaṣrikhun” (and no one calling for help);"},
    {"type": "pair",
     "ar": "فظنوا أنها عاملة عمل «ليس»، والحق أنها للتبرئة، لكنها ملغاة للضرورة.",
     "en": "so they supposed it governs as “laysa” does, whereas the truth is that it is the lā of absolute negation (al-tabriʾa), but cancelled under poetic necessity (ḍarūra)."},
]
