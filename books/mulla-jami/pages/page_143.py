# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 143 (printed ١٤٢)."""

PAGE_NUMBER = 143
PRINTED_PAGE = "١٤٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "بالاسم الظاهر[[١]].",
     "en": "…with the overt noun (al-ism al-ẓāhir)."},
    {"type": "matn",
     "ar": "وأما التنازع الواقع في الضمير المنفصل فعلى مذهب الكسائي يقطع بالحذف، وعلى مذهب الفراء فيعملان معا.",
     "en": "As for the tanāzuʿ that occurs in the detached pronoun: according to the doctrine of al-Kisāʾī it is resolved by elision (ḥadhf), and according to the doctrine of al-Farrāʾ the two [verbs] govern [it] jointly."},
    {"type": "matn",
     "ar": "وأما على مذهب غيرهما فلا يمكن قطعه؛ لأن طريق القطع عندهم[[٢]] الإضمار، وهو ممتنع لما عرفت[[٣]].",
     "en": "But according to the doctrine of others than these two, its resolution is impossible; because the method of resolution according to them is concealment (iḍmār), and that is precluded for the reason you have learned."},
    {"type": "matn",
     "ar": "(فقد يكون[[٤]]) أي: تنازع الفعلين:",
     "en": "(Then it may be—fa-qad yakūnu), that is: the contention of the two verbs [may be]:"},
    {"type": "matn",
     "ar": "١- (في الفاعلية[[٥]]) بأن يقتضي كل منهما أن يكون الاسم الظاهر فاعلا له، فيكونان متفقين في اقتضاء الفاعلية[[٦]]",
     "en": "1. (in agency—fī al-fāʿiliyya), in that each of them requires the overt noun to be its agent (fāʿil), so that the two agree in requiring agency,"},
    {"type": "matn",
     "ar": "(مثل: «ضربني وأكرمني زيد»).",
     "en": "(as in: “Zayd struck me and honored me”—ḍarabanī wa-akramanī Zaydun)."},
    {"type": "matn",
     "ar": "٢- (و) قد يكون تنازعهما (في المفعولية[[٧]]) بأن يقتضي كل منهما أن يكون الاسم",
     "en": "2. (And) their contention may be (in objecthood—fī al-mafʿūliyya), in that each of them requires the noun…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قلت: حكم الاسم الظاهر الواقع بعد «إلا» حكم الضمير المنفصل، فلا بد من تخصيص الظاهر؟",
     "en": "If you say: the rule for the overt noun occurring after “illā” is the rule for the detached pronoun, so must not “the overt [noun]” be restricted?"},
    {"type": "pair",
     "ar": "قلنا: لعل المراد جواز القطع بالإضمار قياسا، لكن لما لم يستعمل إلا بطريق الحذف كان ينبغي أن يحذف.",
     "en": "We say: perhaps what is meant is the permissibility of resolution by concealment by analogy (qiyās); but since it has not been used except by way of elision, it ought to be elided."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: يلزم البصريين في هذا المقام، أي: في مقام «ما ضرب وما أكرم إلا أنا أو إلا زيد» متابعة الكسائي في مذهبه؛",
     "en": "Al-Shaykh al-Raḍī said: the Baṣrans are bound in this situation—that is, in the situation of “None struck and none honored except I” or “…except Zayd”—to follow al-Kisāʾī in his doctrine;"},
    {"type": "pair",
     "ar": "لأنه يوافقونه ههنا في أنه من باب الحذف لا الإضمار؛ إذ لا يستعمل إلا كذلك.",
     "en": "because they agree with him here that it belongs to the category of elision, not concealment; since it is not used except thus."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: والحال أن الإضمار الذي هو طريق القطع عند الجمهور ممتنع فيما ذكر لما عرفت آنفا من لزوم استتار الحرف أو فساد المعنى.",
     "en": "That is: the situation being that concealment, which is the method of resolution according to the majority, is precluded in what has been mentioned, for what you learned just now—namely, that it entails either the concealment of the particle or the corruption of the meaning."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الفاء جزاء الشرط، والجملة جزائية.",
     "en": "The fāʾ [introduces] the apodosis of the condition, and the sentence is an apodosis."},
    {"type": "pair",
     "ar": "ويجوز أن يكون الفاء للاعتراض، والجملة معترضة، والجزاء قوله: فإن أعملت الأول إن كان قوله: ويختار بالواو على ما في أكثر النسخ.",
     "en": "It is also permissible that the fāʾ be parenthetical (li-l-iʿtirāḍ) and the sentence a parenthesis (muʿtariḍa), the apodosis being his words “and if you make the first govern,” if his words “wa-yakhtāru” are with wāw, as in most copies;"},
    {"type": "pair",
     "ar": "وقوله: ويختار إن كان بالفاء على ما في بعض النسخ.",
     "en": "and [the apodosis is] his words “yakhtāru” if it is with fāʾ, as in some copies."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قوله: «فقد يكون» الظاهر بحسب اللفظ أنه جزاء، وبحسب المعنى أنه بيان لأقسام التنازع،",
     "en": "ʿAbd al-Ghafūr said: his words “fa-qad yakūnu”: what is apparent in respect of wording is that it is an apodosis, and in respect of meaning that it is an exposition of the divisions of tanāzuʿ;"},
    {"type": "pair",
     # REVIEW: printed «فإن أعلمت» here (vs. «فإن أعملت» just above); transcribed as printed, translated as أعملت.
     "ar": "وحينئذ يكون الجزاء قوله: فإن أعلمت، أو المقدر الذي هو جاز إعمال كل منهما، أو فيختار كما في بعض النسخ.",
     "en": "in that case the apodosis is his words “and if you make [the first] govern,” or the implied [clause] which is “making each of them govern is permissible,” or “fa-yakhtāru,” as in some copies."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "تفصيل وبيان للتنازع المجمل المذكور في الشرطية.",
     "en": "A detailing and exposition of the tanāzuʿ mentioned in summary in the conditional [sentence]."},
    {"type": "pair",
     "ar": "وجزاء الشرط قوله: «فيختار البصريون إعمال الثاني» إذا كان بالفاء.",
     "en": "The apodosis of the condition is his words “then the Baṣrans choose to make the second govern,” when it is with fāʾ."},
    {"type": "pair",
     "ar": "وأما إذا كان بالواو فقوله: «فقد يكون في الفاعلية» جزاء الشرط.",
     "en": "But when it is with wāw, then his words “then it may be in agency” are the apodosis of the condition."},
    {"type": "pair",
     "ar": "ثم اعلم أن النزاع في مفعول ما لم يسم فاعله داخل في النزاع في الفاعلية، إما باختيار مذهب من جعل مفعول ما لم يسم فاعله داخلا في الفاعل، أو بتعميم الفاعل من أن يكون حقيقيا أو حكميا،",
     "en": "Know, further, that contention over the object of a verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu) falls under contention in agency, either by adopting the doctrine of those who count the object of the verb whose agent is not named as included in the agent, or by generalizing “agent” to cover the real and the notional (ḥukmī);"},
    {"type": "pair",
     "ar": "ولا يجوز إدخاله في المفعولية، فإن إطلاق المفعول على مفعول ما لم يسم فاعله غير شائع لا بالتعميم من الحقيقي والحكمي ولا بغيره.",
     "en": "and it is not permissible to include it under objecthood, for applying the term “object” to the object of a verb whose agent is not named is not current usage, neither by generalizing over the real and the notional nor otherwise."},
    {"type": "pair",
     "ar": "وأيضا على تقدير أن يكون المفعول شاملا لمفعول ما لم يسم فاعله لا بد من إظهاره عند إعمال الثاني واقتضاء الأول مفعول ما لم يسم فاعله عند البصري، مع أنه يضمر في الأول ولا يظهر.",
     "en": "Moreover, on the supposition that “object” includes the object of a verb whose agent is not named, it would have to be made overt, according to the Baṣran, when the second is made to govern and the first requires an object of a verb whose agent is not named; yet it is concealed in the first and not made overt."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وإن اقتضى أحدهما فاعلا حقيقيا، والآخر مفعول ما لم يسم فاعله الذي هو فاعل حكمي.",
     "en": "Even if one of them requires a real agent and the other the object of a verb whose agent is not named, which is a notional agent."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الظاهر أن تعميم المفعولية أيضا من الحقيقي والحكمي، ليتناول التنازع في الحال في قولك: «جاء زيد وضربت عمرا راكبا».",
     "en": "What is apparent is that objecthood too is generalized over the real and the notional, so as to cover contention over the circumstantial qualifier (ḥāl) in your saying: “Zayd came, and I struck ʿAmr, riding.”"},
]
