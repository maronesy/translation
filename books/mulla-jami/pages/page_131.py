# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 131 (printed ١٣٠)."""

PAGE_NUMBER = 131
PRINTED_PAGE = "١٣٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "والمراد تقديمه عليه وجوبا[[١]]؛ ليخرج عنه المبتدأ المقدم عليه خبره، نحو: «كريم من يكرمك».",
     "en": "What is meant is that it be placed before it obligatorily; so as to exclude the mubtadaʾ whose predicate is put before it, as in “Noble is he who honors you.”"},
    {"type": "matn",
     "ar": "فإن قلت: قد يجب تقديمه إذا كان المبتدأ نكرة، والخبر ظرفا، نحو: «في الدار رجل»[[٢]]؟",
     "en": "Now if you say: its being placed first is sometimes obligatory when the mubtadaʾ is indefinite and the predicate is an adverbial, as in “In the house is a man”?"},
    {"type": "matn",
     "ar": "قلت: المراد وجوب تقديم نوعه[[٣]]، وليس نوع الخبر مما يجب تقديمه، بخلاف نوع ما أسند إلى الفاعل.",
     "en": "I say: what is meant is the obligatory precedence of its kind, and the kind of predicate is not something that must be placed first — unlike the kind of that which is predicated of the agent."},
    {"type": "matn",
     "ar": "(على جهة قيامه به) أي: إسنادا واقعا[[٤]] على طريقة قيام الفعل[[٥]]، أو شبهه به،",
     "en": "(By way of its subsisting through it) — that is, as a predication occurring in the manner of the verb’s subsistence, or the [verb-]resembler’s subsistence, through it;"},
    {"type": "matn",
     "ar": "وطريقة قيامه به أن يكون على صيغة المعلوم[[٦]]، أو على ما في حكمها كاسم الفاعل، والصفة المشبهة.",
     "en": "and the manner of its subsisting through it is that it be in the active form (ṣīghat al-maʿlūm), or in what has its ruling, such as the active participle and the assimilate epithet."},
    {"type": "matn",
     "ar": "واحترز بهذا القيد عن مفعول[[٧]] ما لم يسم فاعله[[٨]] كـ«زيد» في «ضرب زيد» على صيغة المجهول،",
     "en": "By this qualifier he guards against the object of a verb whose agent is not named (the deputy-agent) — like “Zayd” in “Zaydun was struck (ḍuriba Zaydun)” in the passive form."},
    {"type": "matn",
     "ar": "والاحتياج إلى هذا القيد إنما هو على مذهب من لم يجعله داخلا في الفاعل كالمصنف.",
     "en": "The need for this qualifier arises only according to the doctrine of one who does not include it [the deputy-agent] within “the agent,” as the author does not."},
    {"type": "matn",
     "ar": "وأما على مذهب من جعله داخلا فيه كصاحب المفصل[[٩]]، فلا حاجة إلى هذا القيد، بل يجب ألا يقيد به.",
     "en": "But according to the doctrine of one who does include it within it — as does the author of al-Mufaṣṣal — there is no need for this qualifier; indeed, it must not be so qualified."},
    {"type": "matn",
     "ar": "(مثل): «زيد» في (قام زيد[[١٠]]). فهذا مثال لما أسند إليه الفعل. (و) مثل: «أبوه» في…",
     "en": "(Such as): “Zayd” in (Zayd stood, qāma Zaydun). This is an example of that to which the verb is predicated. (And) such as: “his father” in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأنه الفرد الكامل، واللفظ إذا أطلق ينصرف إليه.",
     "en": "Because it is the complete instance, and an expression, when used absolutely, is directed to it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيصدق على «رجل» أنه أسند إليه شبه الفعل، أعني الظرف مقدما عليه وجوبا، فيدخل في تعريف الفاعل ما ليس بفاعل.",
     "en": "For it would then be true of “man” that a verb-resembler — namely the adverbial, obligatorily placed before it — has been predicated of it, and so something that is not an agent would enter the definition of the agent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: نوع الفعل أو شبهه المسند إلى ذلك الاسم.",
     "en": "That is: the kind of verb, or of its resembler, that is predicated of that noun."},
    {"type": "pair",
     "ar": "قيل: والقرينة أنه بصدد تعريف نوع من المرفوعات.",
     "en": "It is said: the indication is that he is in the course of defining a kind of the nominatives."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: «على جهة قيامه» متعلق بـ«أسند»، أو صفة لمصدره.",
     "en": "An indication that his words “by way of its subsisting” are governed by “predicated,” or are an attribute of its verbal noun."},
    {"type": "pair",
     "ar": "قيل: يحتمل أن يكون حالا بعد حال، ولا يخلو عن شيء؛ لأن الفعل لا يكون على طريقة القيام، بل الإسناد يكون كذلك.",
     "en": "It is said: it may be a circumstantial clause following [another] circumstantial clause; but this is not free of objection, since the verb is not [what is] “in the manner of subsistence,” rather the predication is so."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: قيام مدلوله، يقال: عملت هذا العمل على وجه عملك، وعلى جهته، أي: على طرزه وطريقته وشكله.",
     "en": "That is, the subsistence of its meaning. One says: “I did this deed in the manner of your deed and by its way,” that is: after its pattern, its manner, and its form."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: ذلك علامتها أو من لوازمها، وذلك لأن القيام ثبوت موجود لأمر، واتصاف ذلك الأمر به، والتعبير عنه ليس إلا بصيغة المعلوم؛ لأن مصدر المجهول لا يوجد أصلا، ومصدر المعلوم قد يوجد لكن فيه تأمل.",
     "en": "That is: it [the active form] is its mark, or one of its concomitants; because subsistence is the establishment of something existent for a matter, and the qualification of that matter by it, and the only way to express it is by the active form — for the passive has no verbal noun at all, whereas the active does have one, though there is [room for] reflection on this."},
    {"type": "pair",
     "ar": "والمراد بالإسناد الذي هو على طريقة القيام ثبوت شيء لأمر ثبوتا يماثل القيام ويشاكله في المعنى، أو في التعبير فتعبيره تعبير القيام.",
     "en": "What is meant by the predication that is “in the manner of subsistence” is the establishing of something for a matter with an establishment that parallels subsistence and resembles it in meaning — or in expression, so that its expression is the expression of subsistence."},
    {"type": "pair",
     "ar": "إن قلت: فعلى هذا يخرج الإسناد الذي هو نفس القيام؟ قلنا: للقيام أفراد بعضها يماثل بعضا.",
     "en": "If you say: on this basis, then, the predication that is subsistence itself would be excluded? We answer: subsistence has instances, some of which parallel others."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ووجه الاحتراز به أن الفعل المجهول واسم المفعول يفيدان وقوع الضرب على المسند إليه.",
     "en": "The point of the guarding by it is that the passive verb and the passive participle both convey the falling of the [act of] striking upon that of which it is predicated."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وإن كان للمصدر المجهول؛ لأنه في قوة «أن» مع الفعل المجهول.",
     "en": "Even though [it may be interpreted as subsisting] by the passive verbal noun, since it has the force of “an” together with the passive verb."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "ومعه الشيخ عبد القاهر وأكثر البصريين.",
     "en": "With him [in this] are al-Shaykh ʿAbd al-Qāhir [al-Jurjānī] and most of the Baṣrans."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أشار بذلك إلى المسامحة الشائعة في مقام التمثيل بذكر الكل مع أن المقصود التمثيل بالجزء.",
     "en": "By this he alluded to the common laxity in the setting of exemplification, whereby the whole is mentioned although what is meant is exemplification by the part."},
]
