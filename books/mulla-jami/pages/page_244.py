# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 244 (printed ٢٤٣)."""

PAGE_NUMBER = 244
PRINTED_PAGE = "٢٤٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وهو الضرب، فإن» from the foot of PDF p. 243.
    {"type": "matn",
     "ar": "التأديب إنما يحصل بالضرب[[١]] ويترتب عليه.",
     "en": "…disciplining is obtained only by striking, and follows upon it."},
    {"type": "matn",
     "ar": "(و«قعدت عن الحرب جبنا»[[٢]]) مثال لما فعل بسبب وجوده فعل وهو القعود، فإن القعود إنما وقع بسبب الجبن،",
     "en": "(And “I held back from war out of cowardice”) is an example of that because of whose existence an action, namely holding back, is done; for the holding back occurred only because of cowardice."},
    {"type": "matn",
     "ar": "والقائل[[٣]] بكون المفعول له معمولا مستقلا غير داخل في المفعول المطلق يخالف (خلافا) ظاهرا (للزجاج[[٤]]، فإنه) أي: المفعول له (عنده) أي: عند الزجاج (مصدر[[٥]]) من غير لفظ فعله،",
     "en": "Whoever holds that the object of purpose is an independent governed element, not included in the absolute object (al-mafʿūl al-muṭlaq), differs (in disagreement), plainly, (with al-Zajjāj; for it), that is, the object of purpose, (in his view), that is, in al-Zajjāj’s view, (is a maṣdar) not from the wording of its verb;"},
    {"type": "matn",
     "ar": "فالمعنى عنده في المثالين المذكورين: «أدبته بالضرب تأديبا، وجبنت في القعود عن الحرب جبنا»[[٦]]، أو «ضربته ضرب تأديب، وقعدت قعود جبن»[[٧]].",
     "en": "so in his view the meaning in the two examples mentioned is: “I disciplined him by striking, a disciplining, and I was cowardly in holding back from war, a cowardice,” or “I struck him a striking of discipline, and I held back a holding back of cowardice.”"},
    {"type": "matn",
     "ar": "ورد قول الزجاج[[٨]] بأن صحة تأويل نوع بنوع لا تدخله في حقيقته.",
     "en": "Al-Zajjāj’s view has been rejected on the ground that the soundness of interpreting one kind by another kind does not bring it into the latter’s reality."},
    {"type": "matn",
     "ar": "ألا ترى إلى صحة تأويل الحال بالظرف من حيث إن معنى «جاء زيد راكبا» جاء زيد وقت الركوب من غير أن تخرج عن حقيقتها.",
     "en": "Do you not see that the circumstantial accusative (ḥāl) may soundly be interpreted as an adverb of time (ẓarf), in that the meaning of “Zayd came riding” is “Zayd came at the time of riding,” without its leaving its own reality?"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قلت: كيف يحصل التأديب بالضرب، ويترتب عليه مع اتحادهما بحسب الذات؟",
     "en": "If you say: how can disciplining be obtained by striking and follow upon it, when the two are one in essence?"},
    {"type": "pair",
     "ar": "قلنا: أراد ترتب ما يتضمنه التأديب، أعني: التأدب.",
     "en": "We say: he meant the following-upon of what disciplining entails, namely becoming disciplined (taʾaddub)."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: العلة الحاملة التأدب، وإنما نصب التأديب لتضمنه العلة الحقيقية، ومشاركته الحدث في الفاعل والزمان.",
     "en": "Shaykh al-Raḍī said: the motivating cause is becoming disciplined; “disciplining” is put in the accusative only because it entails the real cause and shares with the event [the verb] its agent and time."},
    {"type": "pair",
     "ar": "ولو صرحت بالعلة الحقيقية لم ينتصب عند النحاة.",
     "en": "Were you to state the real cause explicitly, it would not take the accusative according to the grammarians."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: ولو قال وجاريته شجاعة لكان أحسن أي: أحسن بمقام المنازعة للزجاج، وإظهار الجلادة،",
     "en": "It has been said: had he said “and I engaged him out of courage,” it would have been better, that is, better suited to the setting of disputing with al-Zajjāj and to displaying firmness."},
    {"type": "pair",
     "ar": "ويحتمل أن يقال فيه تعريض عليه وتنبيه على عدم دقته، والاكتفاء بظاهر الأمر.",
     "en": "It may be said that there is in it an oblique hint at him and an alert to his lack of precision and his contenting himself with the outward aspect of the matter."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "والقول بكون المفعول له مفهوما مستقلا، كما هو المفهوم من الكلام يخالف خلافا لقول الزجاج.",
     "en": "The view that the object of purpose is an independent concept, as is understood from the text, is in disagreement with al-Zajjāj’s view."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا فائدة لقوله: ظاهرا.",
     "en": "His word “plainly” serves no purpose."},
    {"type": "pair",
     "ar": "والأظهر أن يقدر: يخالف الزجاج هذا القائل خلافا؛ لأن قول النحاة أصل، والخلاف إنما وقع منه.",
     "en": "It is more evident to supply: “al-Zajjāj disagrees with this proponent in disagreement,” because the grammarians’ view is the base, and the disagreement arose only from him."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لما رأى من كون مضمون عامل المفعول له تفصيلا وبيانا له كما في «ضربت تأديبا»، فإن معناه: أدبت بالضرب تأديبا.",
     "en": "Because he saw that the content of the governor of the object of purpose is a detailing and explanation of it, as in “I struck for discipline,” whose meaning is “I disciplined by striking, a disciplining.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن القعود مغاير بالذات للجبن، فإنه مقدم على القعود بحسب التحقق، فكيف يصح أن يكون مصدرا مغايرا للفظ فعله",
     "en": "Against this: holding back is essentially different from cowardice, for [cowardice] precedes holding back in realization; so how can it be a maṣdar differing from the wording of its verb?"},
    {"type": "pair",
     "ar": "اللهم إلا أن يراد بالجبن أثر الكيفية القائمة بالنفس، وهو القعود عن الحرب",
     "en": "Unless by cowardice is meant the effect of the quality subsisting in the soul, namely holding back from war,"},
    {"type": "pair",
     "ar": "كما قد يراد بالشجاعة الأثر المترتب على الكيفية النفسانية، وهو الإقدام.",
     "en": "just as by courage is sometimes meant the effect following upon the psychic quality, namely advancing [into battle]."},
    {"type": "pair",
     "ar": "ولا يخفى أن في ذلك مخالفة من وجه آخر.",
     "en": "It is not hidden that in this there is a departure in another respect."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الظاهر أن المصدر حقيقة هو المحذوف لا المذكور.",
     "en": "It appears that the maṣdar in reality is the elided one, not the one mentioned."},
    {"type": "pair",
     "ar": "وإطلاق المصدر عليه لنيابته عن المحذوف كما في «ضربته سوطا» أي: ضرب سوط،",
     "en": "The term maṣdar is applied to it because it stands in for the elided one, as in “I struck him a whip,” that is, a striking of a whip;"},
    {"type": "pair",
     "ar": "فالقول بأنه على هذا التقدير مصدر من غير لفظ فعله لا يخلو عن شيء.",
     "en": "so the claim that, on this supposition, it is a maṣdar not from the wording of its verb is not free of difficulty."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ورده المصنف أيضا بأن معنى ضربته تأديبا ضربته للتأديب اتفاقا.",
     "en": "The author also rejected it on the ground that the meaning of “I struck him for discipline” is, by agreement, “I struck him for the purpose of disciplining.”"},
    {"type": "pair",
     "ar": "وقولك: للتأديب ليس بمفعول مطلق، فكذا تأديبا الذي بمعناه.",
     "en": "And your words “for the purpose of disciplining” are not an absolute object; so likewise “for discipline,” which has its meaning."},
]
