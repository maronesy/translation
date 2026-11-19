# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 389 (printed ٣٨٨)."""

PAGE_NUMBER = 389
PRINTED_PAGE = "٣٨٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «والثانية: أن «ما» معناه: «أي شيء»، و«ذا» زائدة.» at the foot of PDF p. 388 (new sentence).
    {"type": "matn",
     "ar": "والظاهر أن مؤداهما واحد[[١]]، فإن معنى قولهم: «إنها بكمالهما بمعنى: «أي شيء» أنه ليس لكل منهما معنى بالاستقلال؛ لكون كلمة «ذا» زائدة، فالمفهوم من مجموعهما «أي شيء»",
     "en": "What is apparent is that the two come to the same thing, for the meaning of their saying “it, the two of them together, means ‘ayyu shayʾin’” is that neither of them has a meaning on its own, because the word “dhā” is redundant; so what is understood from the two together is “ayyu shayʾin”."},
    {"type": "matn",
     "ar": "(و) حينئذ (جوابه: نصب[[٢]]) أي: منصوب على أنه مفعول لفعل محذوف، كما إذا قلت: «الإكرام» أي: صنعت الإكرام",
     "en": "(And) in that case (its answer is in the accusative), that is, accusative as the object of an elided verb, as when you say “al-ikrāma”, that is, “ṣanaʿtu al-ikrāma” (I did honouring),"},
    {"type": "matn",
     "ar": "ليكون الجواب مطابقا للسؤال في كون كل منهما جملة فعلية،",
     "en": "so that the answer corresponds to the question in each of them being a verbal sentence."},
    {"type": "matn",
     "ar": "ويجوز في الأول نصب الجواب بتقدير الفعل المذكور، وفي الثاني رفعه على أن يكون خبر مبتدأ محذوف،",
     "en": "On the first [analysis] the answer may be in the accusative by supposing the verb mentioned, and on the second it may be in the nominative as the predicate of an elided subject;"},
    {"type": "matn",
     "ar": "ولم يعتبره المصنف، لفوات المطابقة بين السؤال والجواب.",
     "en": "but the author did not take this into account, because correspondence between question and answer is lost."},

    {"type": "section", "ar": "[أسماء الأفعال]",
     "en": "Verbal Nouns (Asmāʾ al-Afʿāl)"},

    {"type": "matn",
     "ar": "(أسماء الأفعال: ما كان) أي: اسم كان[[٣]] (بمعنى الأمر أو الماضي[[٤]]) اللذين هما من أقسام مبني الأصل",
     "en": "(Verbal nouns (asmāʾ al-afʿāl) are what is), that is, a noun that is, (in the sense of the imperative or the past) (the two of which are among the kinds of what is indeclinable in origin);"},
    {"type": "matn",
     "ar": "فعلة بنائها كونها مشابهة لمبني الأصل، فما قيل: «أف» بمعنى",
     "en": "so the cause of their indeclinability is their resembling what is indeclinable in origin. As for what has been said, that “uffin” in the sense of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يؤيده ما نقلناه عن الشيخ الرضي من أن «ذا» موصولة أو زائدة.",
     "en": "This is supported by what we have quoted from Shaykh al-Raḍī, that “dhā” is either relative or redundant."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هذا إذا كان بعد «ذا» فعل ناصب لما قبله، أو مشتغل عنه بضميره، أو متعلقه",
     "en": "This is when after “dhā” there is a verb that governs what precedes it in the accusative, or that is diverted from it by its pronoun or by something connected with it."},
    {"type": "pair",
     "ar": "أما إذا لم يكن كذلك نحو: ماذا عرض عليهم، وماذا أحل لهم، فالرفع لازم سواء جعلت «ذا» موصولة أو زائدة.",
     "en": "But when it is not so, as in “mādhā ʿuriḍa ʿalayhim?” (what was presented to them?) and “mādhā uḥilla lahum?” (what was made lawful for them?), the nominative is necessary, whether you make “dhā” relative or redundant."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: «كأن» printed (clear at 700 dpi); fn. ٤ has «كان هذه تحتمل», so «كان» seems intended; transcribed as printed.
    {"type": "pair",
     "ar": "الظاهر أي: أسماء يقال كأن هذه يحتمل التمام والنقصان والصيرورة والزيادة. ولا يخفى أن الثابت أنسب،",
     "en": "The more apparent [gloss] is “that is, nouns”. It is said that this “kāna” [printed “kaʾanna”] admits being complete, incomplete, in the sense of becoming, and redundant. It is not hidden that [the sense of] being established is the more fitting."},
    {"type": "pair",
     "ar": "ومن حق أسماء الأفعال ألا يكون لها إعراب كالماضي والأمر.",
     "en": "It is due to verbal nouns that they have no inflection, like the past and the imperative."},
    {"type": "pair",
     "ar": "وقيل: هي مرفوع المحل بالابتداء، فهو مبتدأ فاعله سد مسد الخبر كما في قولنا: «أقائم زيد»،",
     "en": "It has been said: they are nominative in position as subjects, so [each] is a subject whose agent stands in place of the predicate, as in our saying “a-qāʾimun Zaydun?” (is Zayd standing?)."},
    {"type": "pair",
     "ar": "وهذا هو الذي اختاره المصنف في إيضاح المفصل، وإن فاته بيان المبتدأ في هذا الكتاب.",
     "en": "This is what the author chose in Īḍāḥ al-Mufaṣṣal, even though he omitted to explain [this kind of] subject in this book."},
    {"type": "pair",
     "ar": "وقيل: هي مصادر منصوبة بأفعال محذوفة، وينافي تقدير الفعل كونها اسم فعل.",
     "en": "It has also been said: they are verbal nouns (maṣādir) in the accusative governed by elided verbs; but supposing the verb is incompatible with their being verbal nouns of the asmāʾ al-afʿāl kind."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيل: كان هذه تحتمل أن تكون ناقصة على أصلها، وتامة بمعنى صار، وزائدة.",
     "en": "It has been said: this “kāna” may be incomplete, as is its basic use, or complete in the sense of “became”, or redundant."},
    {"type": "pair",
     "ar": "ولما كانت أسماء الأفعال بمعنى الأمر أو الماضي كان حقها ألا يكون لها محل من الإعراب كالأمر والماضي.",
     "en": "Since verbal nouns have the sense of the imperative or the past, it is due to them that they have no position in inflection, like the imperative and the past."},
    {"type": "pair",
     "ar": "وقيل: إنها مصادر، وفيه أنها تستدعي تقدير فعل قبلها فلا تكون أسماء أفعال.",
     "en": "It has been said that they are maṣādir; against this, they would then require supposing a verb before them, and so would not be verbal nouns."},
    {"type": "pair",
     "ar": "وفيه أن القائل بذلك لا يقول: إنها أسماء الأفعال، بل يقول: إنها أسماء مصادر الأفعال، وإنما سميت أسماء الأفعال قصرا للمسافة.",
     "en": "Against this: whoever holds that view does not say that they are names of the verbs; rather he says that they are names of the maṣādir of the verbs, and they were called asmāʾ al-afʿāl only to shorten the way."},
    {"type": "pair",
     "ar": "ولكن فيه أن لا وجه لبنائها، اللهم إلا أن يقال: إن بعضها مبني لكونها في الأصل أصواتا كـ«صه ومه»، وحمل الباقي عليها طردا للباب.",
     "en": "But against this, there is then no reason for their indeclinability—unless it be said that some of them are indeclinable because they were originally sounds, like “ṣah” and “mah”, and the rest were assimilated to them for the regularity of the class."},
    {"type": "pair",
     "ar": "وقيل: إنه مبتدأ والفاعل ساد مسد الخبر. وفيه أن معنى الفعل ينافي الابتداء.",
     "en": "It has been said: [such a noun] is a subject, and the agent stands in place of the predicate. Against this: the sense of the verb is incompatible with being a subject."},
    {"type": "pair",
     "ar": "وفيه أن هذا القسم من المبتدأ لكونه مسندا لا ينافيه معنى الفعل.",
     "en": "Against this: this kind of subject, being a predicate-bearer (musnad), is not incompatible with the sense of the verb."},
    {"type": "pair",
     "ar": "وفيه أن معنى الفعل لو لم يناف للابتداء لصح أن يقال لكل فعل: إنه مبتدأ.",
     "en": "Against this: were the sense of the verb not incompatible with being a subject, it would be valid to say of every verb that it is a subject."},
    {"type": "pair",
     "ar": "وفيه أن ذلك أمر اصطلاحي، وأن هذا القسم من المبتدأ ثابت بحسب الضرورة، ولا ضرورة في الأفعال لجواز ألا يكون لها محل من الإعراب بخلاف الاسم،",
     "en": "Against this: that is a matter of convention, and this kind of subject is established out of necessity; there is no necessity in the case of verbs, since they may have no position in inflection, unlike the noun,"},
    {"type": "pair",
     "ar": "فإن خلوه عن الإعراب غير معهود، فلا بد أن يخرج له وجه.",
     "en": "for its being devoid of inflection is unknown, so some account must be found for it."},
    {"type": "pair",
     "ar": "نعم للخصم أن يقول: إن القسم الثاني من المبتدأ يؤول بالآخرة إلى أنه مسند إليه؛ لأن قولك: أقائم زيد في قوة: أن صاحب القيام هو زيد، ولا يتصور ذلك في الفعل وما هو بمعناه.",
     "en": "Yes, the opponent may say: the second kind of subject comes in the end to being the thing predicated of (musnad ilayhi), because your saying “a-qāʾimun Zaydun?” is equivalent to “the one who has the standing is Zayd”; and that cannot be conceived for the verb and what has its meaning."},
    {"type": "pair",
     "ar": "ولهذا جعل بعضهم عامل الرفع في المبتدأ مطلقا كونه مسندا إليه.",
     "en": "For this reason some made the governor of the nominative in the subject, without qualification, its being the thing predicated of."},
]
