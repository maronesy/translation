# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 148 (printed ١٤٧)."""

PAGE_NUMBER = 148
PRINTED_PAGE = "١٤٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "القيس الذي هو أفصح شعراء العرب أعمل الأول، فلو لم يكن إعمال الأول أولى لما اختاره؛ إذ لا قائل بتساوي الإعمالين[[١]].",
     "en": "…al-Qays, who is the most eloquent of the poets of the Arabs, made the first govern; and had making the first govern not been preferable he would not have chosen it, since no one holds that the two governments are equal."},
    {"type": "matn",
     "ar": "فأجاب المصنف[[٢]] عن طرف البصريين وقال: (وقول امرئ القيس[[٣]]: «كفاني ولم أطلب قليل من المال» ليس منه) أي: من باب التنازع",
     "en": "So the author answered on behalf of the Baṣrans, saying: (The verse of Imruʾ al-Qays, “a little wealth would have sufficed me, and I would not have sought,” is not of it—wa-qawlu Imriʾ al-Qays … laysa minhu), that is: not of the category of tanāzuʿ,"},
    {"type": "matn",
     "ar": "(لفساد المعنى) على تقدير توجه كل من «كفاني ولم أطلب»[[٤]] إلى «قليل من المال»",
     "en": "(because of the corruption of the meaning—li-fasād al-maʿnā) on the supposition that each of “kafānī” and “lam aṭlub” is directed to “qalīlun min al-māl,”"},
    {"type": "matn",
     "ar": "لاستلزامه عدم السعي[[٥]] لأدنى معيشة، وانتفاء كفاية قليل من المال، وثبوت طلبه المنافي لكل منهما[[٦]]،",
     "en": "since it would entail his not striving for the meanest livelihood, and the absence of the sufficiency of a little wealth, and the affirmation of his seeking it, which is incompatible with each of these two;"},
    {"type": "matn",
     "ar": "وذلك لأن لفظ «لو» يجعل مدخوله المثبت شرطا كان أو جزاء أو معطوفا على أحدهما منفيا، والمنفي من ذلك مثبتا.",
     "en": "that is because the word “law” renders what it enters upon, if affirmative—whether condition, apodosis, or conjoined to one of them—negated, and the negated among these affirmed."},
    {"type": "matn",
     "ar": "فعلى هذا ينبغي أن يكون مفعول «لم أطلب» محذوفا، أي: «لم أطلب العز والمجد» كما يدل عليه البيت المتأخر، أعني قوله:",
     "en": "On this basis, the object of “lam aṭlub” must be elided, that is: “I would not have sought glory and nobility,” as the later verse indicates, I mean his words:"},
    {"type": "verse",
     "ar": "ولكنما أسعى لمجد مؤثل          وقد يدرك المجد المؤثل أمثالي",
     "en": "But I strive only for deep-rooted nobility, and men like me may attain deep-rooted nobility."},
    {"type": "matn",
     "ar": "وحينئذ يستقيم المعنى، يعني: «أنا لا أسعى لأدني معيشة، ولا يكفيني قليل من المال، ولكني أطلب المجد الأصيل الثابت، وأسعى له».",
     "en": "In that case the meaning is sound; he means: “I do not strive for the meanest livelihood, and a little wealth does not suffice me; but I seek nobility, deep-rooted and firm, and strive for it.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أنه يجوز أن يكون امرؤ القيس يسوي الإعمالين، لكنه اختار الأول لاستلزامه ما هو الواجب.",
     "en": "There is [an objection] to this: it is possible that Imruʾ al-Qays regarded the two governments as equal, but chose the first because it entails what is required."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جواب لما، وإتيان الفاء في جوابه الماضي لفظا واقع قليلا، كذا فهم من الرضي في بحث الظروف.",
     "en": "[It is] the apodosis of “lammā”; the use of fāʾ in its apodosis when it is past in form occurs rarely—so it is understood from al-Raḍī in the discussion of adverbs (al-ẓurūf)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "صرح باسمه تنبيها على قوة الاستشهاد، وضرورة الجواب عنه. وقوله: «كفاني» بدل أو بيان لقول.",
     "en": "He named him explicitly to draw attention to the strength of the citation as evidence and the necessity of answering it. His words “kafānī” are a substitute (badal) for, or an explication (bayān) of, “qawl.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إن قلت: هذا إذا كان «لم أطلب» معطوفا على «كفاني».",
     "en": "If you say: this [holds] when “lam aṭlub” is conjoined to “kafānī.”"},
    {"type": "pair",
     "ar": "وأما إذا كانت الجملة حالية، أو معترضة، أو معطوفة على الشرطية. فلا يلزم هذا الفساد؟",
     "en": "But when the sentence is circumstantial (ḥāliyya), or parenthetical, or conjoined to the conditional sentence, then this corruption is not entailed?"},
    {"type": "pair",
     "ar": "قلنا: لا يجوز الأول للزوم تقييد الجزاء بنقيض الشرط، ولا الأخيران للزوم حمل الكلام على التأكيد دون التأسيس مع أن واو العطف والاعتراض ينبو عن ذلك.",
     "en": "We say: the first is not permissible, since it entails qualifying the apodosis by the contradictory of the condition; nor are the last two, since they entail taking the statement as corroboration (taʾkīd) rather than as establishing [a new meaning] (taʾsīs), while the wāw of conjunction and of parenthesis is at odds with that."},
    {"type": "pair",
     "ar": "وذلك لأن نفي السعي مستلزم لنفي الطلب.",
     "en": "That is because the negation of striving entails the negation of seeking."},
    {"type": "pair",
     "ar": "إن قلت: السعي الطلب البليغ، فيكون أخص من الطلب، ونفي الخاص لا يستلزم نفي العام؟",
     "en": "If you say: striving is intense seeking, so it is more specific than seeking, and the negation of the specific does not entail the negation of the general?"},
    {"type": "pair",
     "ar": "قلنا: المراد بالسعي هنا الطلب مطلقا؛ لأن الكفاية تحتاج إلى الطلب لا إلى الطلب البليغ.",
     "en": "We say: what is meant by striving here is seeking absolutely; because sufficiency requires seeking, not intense seeking."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وجعل نقيض الشرط جزاء له.",
     "en": "And making the contradictory of the condition its apodosis."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أما منافاته لعدم السعي، فلما مر من أن المراد من السعي الطلب.",
     "en": "As for its incompatibility with the absence of striving, it is because of what has passed, that what is meant by striving is seeking."},
    {"type": "pair",
     "ar": "وأما منافاته لعدم الكفاية، فلما يدل عليه صريح الشرطية.",
     "en": "As for its incompatibility with the absence of sufficiency, it is because of what the explicit wording of the conditional indicates."},
]
