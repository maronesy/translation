# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 67 (printed ٦٦)."""

PAGE_NUMBER = 67
PRINTED_PAGE = "٦٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "فتي، وفتيا، وبفتي[[١]]، انقلبت الياء ألفا، فصار الإعراب تقديريا.",
     "en": "[As in] futiya, futiyā, and bi-futiya: the yāʾ has been turned into an alif, so the inflection (iʿrāb) becomes implicit (taqdīrī)."},
    {"type": "matn",
     "ar": "والاختلاف اللفظي والتقديري أعم من أن يكون حقيقة أو حكما، كما أشرنا إليه،",
     "en": "The difference — whether overt (lafẓī) or implicit (taqdīrī) — is more general than being either real (ḥaqīqatan) or merely by legal reckoning (ḥukman), as we have already indicated,"},
    {"type": "matn",
     "ar": "لئلا ينتقض بمثل قولنا: «رأيت أحمد»، و«مررت بأحمد»[[٢]]، وقولنا: «رأيت مسلمين، ومررت بمسلمين»[[٣]]، مثنى أو مجموعا.",
     "en": "so that [the definition] is not vitiated by such [examples] as our saying “raʾaytu Aḥmada” (“I saw Aḥmad”) and “marartu bi-Aḥmada” (“I passed by Aḥmad”), and our saying “raʾaytu muslimīna” and “marartu bi-muslimīna”, be it dual or plural."},
    {"type": "matn",
     "ar": "فإنه قد اختلف العوامل فيه في العمل، ولا اختلاف في آخر «أحمد» حقيقة بل حكما،",
     "en": "For the governing agents (ʿawāmil) over it do indeed differ in their governance, yet there is no difference in the ending of “Aḥmad” in reality, but only by legal reckoning;"},
    {"type": "matn",
     "ar": "فإن فتحة «أحمد» بعد الناصب علامة النصب[[٤]]، وبعد الجار علامة الجر،",
     "en": "for the fatḥa of “Aḥmad” after the accusative-governing agent (nāṣib) is the marker of the accusative (naṣb), while after the genitive-governing agent (jārr) it is the marker of the genitive (jarr),"},
    {"type": "matn",
     "ar": "وكذا الحال في التثنية والجمع، فآخر المعرب في هذه الصور يختلف باختلاف العوامل حكما لا حقيقة.",
     "en": "and likewise is the case in the dual and the plural. So the ending of the declinable noun (muʿrab) in these instances varies with the variation of the governing agents by legal reckoning, not in reality."},
    {"type": "matn",
     "ar": "فإن قلت[[٥]]: لا يتحقق الاختلاف لا في آخر المعرب، ولا في العوامل[[٦]] إذا ركب بعض الأسماء المعدودة الغير المشابهة لمبني الأصل مع عامله ابتداء[[٧]]؛ ويترتب عليه",
     "en": "If you say: No difference is realized — neither in the ending of the declinable noun nor in the governing agents — when one of the enumerated nouns that do not resemble that which is intrinsically indeclinable (mabnī al-aṣl) is combined with its governing agent from the outset (ibtidāʾan); and there follows upon it —"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ذكر الباء لئلا يسوي المبتدئ بينه وبين فتي لاتخاذهما خطا.",
     "en": "The bāʾ is mentioned lest the beginner equate it (bi-futiya) with futiya, on account of the two being identical in written form (khaṭṭ)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ورأيت حبلى، ومررت بحبلى.",
     "en": "And [likewise]: “raʾaytu ḥublā” (“I saw a pregnant woman”) and “marartu bi-ḥublā” (“I passed by a pregnant woman”)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: مدلول هاتين الصورتين، فإذن يظهر شموله للمثنى والمجموع.",
     "en": "That is: the referent of these two forms; hence its inclusion of the dual and the plural becomes evident."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: علامة هي النصب الذي دل على المفعولية، وقس عليه علامة الجر.",
     "en": "That is: a marker which is the accusative that indicates object-hood (mafʿūliyya); and measure the marker of the genitive against it likewise."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سواء أريد بالعوامل الجماعة، أو ما فوق الواحد.",
     "en": "Whether by “the governing agents” a group is intended, or [merely] more than one."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إلى قوله: مع عامله ابتداء.",
     "en": "[This runs] up to his words: “with its governing agent from the outset.”"},
    {"type": "pair",
     "ar": "إن قلت: التركيب مع العامل لا يكون إلا إذا كان العامل لفظيا، فيجوز أن يكون التركيب مع العامل ابتداء مسبوقا بالتركيب الذي يتحقق معه عاملان معنويان، فيتحقق الاختلاف في آخر المعرب وفي العوامل؟",
     "en": "If you say: Combination with a governing agent occurs only when the agent is an overt one (lafẓī); so it is possible that combination with the agent from the outset be preceded by a combination with which two abstract (maʿnawī) agents are realized, whereby a difference is realized both in the ending of the declinable noun and in the governing agents?"},
    {"type": "pair",
     "ar": "أجيب: بأن المراد باختلاف العوامل كما مر اختلافها في العمل.",
     "en": "The reply is: What is intended by “the difference of the governing agents” is, as has already passed, their difference in governance."},
    {"type": "pair",
     "ar": "وذلك لا يوجد فيما فرض؛ لأن عمل العامل المعنوي ليس إلا الرفع.",
     "en": "And that is not found in the case supposed, because the governance of the abstract agent is nothing but the nominative (rafʿ)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: إذا ركب كائنا مع عامله، ومتحققا معه.",
     "en": "That is: when it is combined as existing together with its governing agent and as realized along with it."},
    {"type": "pair",
     "ar": "فقوله «مع» ليس ظرفا للتركيب، ومن جعله ظرفا للتركيب أورد عليه أن التركيب مع العامل لا يكون إلا إذا كان لفظيا، فيجوز أن يكون التركيب مع العامل ابتداء، ويتحقق اختلاف العوامل لسبق عاملين معنويين؛ فيتحقق الاختلاف في آخر المعرب وفي العوامل.",
     "en": "So his word “with” (maʿa) is not an adverbial qualifier (ẓarf) of the combination; and whoever takes it as an adverbial qualifier of the combination has this objection raised against him: that combination with the agent occurs only when it is overt (lafẓī), so it is possible that combination with the agent be from the outset while the difference of the agents is realized by the precedence of two abstract agents, whereupon a difference is realized in the ending of the declinable noun and in the governing agents."},
    {"type": "pair",
     "ar": "وأجاب عنه: بأنه لا يتحقق بعاملين معنويين، وعامل لفظي اختلاف العوامل؛ إذ لا اختلاف في العمل بين عاملين معنويين هذا.",
     "en": "He answered it: that the difference of the agents is not realized by two abstract agents together with an overt agent, since there is no difference in governance between two abstract agents. So much for that."},
    {"type": "pair",
     "ar": "وفيه نظر من وجوه:",
     "en": "But this is open to question on several counts:"},
    {"type": "pair",
     "ar": "الأول: أن المراد بالعوامل ما فوق الواحد، كما لا يخفى.",
     "en": "First: that what is meant by “the agents” is more than one, as is not hidden."},
    {"type": "pair",
     "ar": "والثاني: أنه لا يصح قول الشارح ليس فيه اختلاف الآخر ولا اختلاف العوامل لتحقق اختلاف الآخر.",
     "en": "Second: that the commentator’s statement — “there is in it neither difference of the ending nor difference of the agents” — is not valid, because the difference of the ending is realized."},
    {"type": "pair",
     "ar": "والثالث: أن العامل المعنوي لا ينحصر في عامل الرفع. وإنما ينحصر فيه عامل ليس معنى الفعل، وللعامل المعنوي الذي هو معنى الفعل أقسام متعددة ناصبة للظرف والمفعول معه.",
     "en": "Third: that the abstract agent is not confined to the agent of the nominative. Rather, what is confined to it [the nominative] is an agent that is not the meaning of the verb; whereas the abstract agent that is the meaning of the verb has numerous kinds that govern in the accusative the adverbial (ẓarf) and the object-of-accompaniment (mafʿūl maʿahu)."},
    {"type": "pair",
     "ar": "والرابع: أنه لا اتجاه للسؤال؛ لأنه لم يقل: كلما ركب مع عامله ابتداء حتى يتجه شيء عليه. لا تقول:",
     "en": "Fourth: that the question has no bearing, because he did not say “whenever it is combined with its agent from the outset,” such that anything might be directed against it. You do not say:"},
]
